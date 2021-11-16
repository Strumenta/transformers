import sys
import json
from antlr4 import *
from pli.PLILexer import PLILexer
from pli.PLIParser import PLIParser
from pli.PLIVisitor import PLIVisitor

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.tensorboard import SummaryWriter
from torchtext.data import Field, TabularDataset, BucketIterator
from jinja2 import Template

global level
# Training hyperparameters
num_epochs = 250
learning_rate = 3e-4
batch_size = 32


# transformer
class Transformer(nn.Module):
    def __init__(
            self,
            embedding_size,
            src_vocab_size,
            trg_vocab_size,
            src_pad_idx,
            num_heads,
            num_encoder_layers,
            num_decoder_layers,
            forward_expansion,
            dropout,
            max_len,
            device,
    ):
        super(Transformer, self).__init__()
        self.src_word_embedding = nn.Embedding(src_vocab_size, embedding_size)
        self.src_position_embedding = nn.Embedding(max_len, embedding_size)
        self.trg_word_embedding = nn.Embedding(trg_vocab_size, embedding_size)
        self.trg_position_embedding = nn.Embedding(max_len, embedding_size)

        self.device = device
        self.transformer = nn.Transformer(
            embedding_size,
            num_heads,
            num_encoder_layers,
            num_decoder_layers,
            forward_expansion,
            dropout,
        )
        self.fc_out = nn.Linear(embedding_size, trg_vocab_size)
        self.dropout = nn.Dropout(dropout)
        self.src_pad_idx = src_pad_idx

    def make_src_mask(self, src):
        src_mask = src.transpose(0, 1) == self.src_pad_idx

        # (N, src_len)
        return src_mask.to(self.device)

    def forward(self, src, trg):
        src_seq_length, N = src.shape
        trg_seq_length, N = trg.shape

        src_positions = (
            torch.arange(0, src_seq_length)
                .unsqueeze(1)
                .expand(src_seq_length, N)
                .to(self.device)
        )

        trg_positions = (
            torch.arange(0, trg_seq_length)
                .unsqueeze(1)
                .expand(trg_seq_length, N)
                .to(self.device)
        )

        embed_src = self.dropout(
            (self.src_word_embedding(src) + self.src_position_embedding(src_positions))
        )
        embed_trg = self.dropout(
            (self.trg_word_embedding(trg) + self.trg_position_embedding(trg_positions))
        )

        src_padding_mask = self.make_src_mask(src)
        trg_mask = self.transformer.generate_square_subsequent_mask(trg_seq_length).to(
            self.device
        )

        out = self.transformer(
            embed_src,
            embed_trg,
            src_key_padding_mask=src_padding_mask,
            tgt_mask=trg_mask,
        )
        out = self.fc_out(out)
        return out


def remove_eos(witheos):
    noeos = []
    for w in witheos:
        if w != '<eos>':
            noeos.append(w)
    return " ".join(noeos)


def save_checkpoint(state, filename="checkpoint.pth.tar"):
    print("=> Saving checkpoint")
    torch.save(state, filename)


def load_checkpoint(checkpoint, model, optimizer):
    print("=> Loading checkpoint")
    model.load_state_dict(checkpoint["state_dict"])
    optimizer.load_state_dict(checkpoint["optimizer"])


def translate_sequence(sentence, pli, ktl, device, max_length=50):
    if type(sentence) == str:
        tokens = [token.lower() for token in sentence.split()]
    else:
        tokens = [token.lower() for token in sentence]
    # Add <SOS> and <EOS> in beginning and end respectively

    tokens.insert(0, pli.init_token)
    tokens.append(pli.eos_token)

    # Iterate  each languae token and convert to an index
    text_to_indices = [pli.vocab.stoi[token] for token in tokens]

    # Convert to Tensor
    sentence_tensor = torch.LongTensor(text_to_indices).unsqueeze(1).to(device)

    outputs = [ktl.vocab.stoi["<sos>"]]
    for i in range(max_length):
        trg_tensor = torch.LongTensor(outputs).unsqueeze(1).to(device)

        with torch.no_grad():
            output = model(sentence_tensor, trg_tensor)

        best_guess = output.argmax(2)[-1, :].item()
        outputs.append(best_guess)

        if best_guess == ktl.vocab.stoi["<eos>"]:
            break

    translated_sentence = [ktl.vocab.itos[idx] for idx in outputs]
    # remove start token
    return translated_sentence[1:]


def transpile_sequence(translated, level):
    tokens = translated["code"]
    data = translated["context"]
    lint = []

    for t in tokens:
        spacer = "".rjust(level * 4)
        if t == "{":
            level += 1
        elif t == "}" and level > 0:
            level -= 1
            spacer = "".rjust(level * 4)

        if t != "<eos>":
            lint.append(spacer + t)

    code = " ".join(lint)
    t = Template(code)

    return t.render(data), level


tokenizer = lambda x: x.split()

pli = Field(sequential=True, use_vocab=True, tokenize=tokenizer, lower=True, init_token="<sos>", eos_token="<eos>")
ktl = Field(sequential=True, use_vocab=True, tokenize=tokenizer, lower=True, init_token="<sos>", eos_token="<eos>")

fields = {'pli': ('p', pli), 'ktl': ('k', ktl)}

train, test = TabularDataset.splits(
    path='data',
    train='train.json',
    test='test.json',
    format='json',
    fields=fields
)

pli.build_vocab(train, max_size=10000, min_freq=1)
ktl.build_vocab(train, max_size=10000, min_freq=1)

# ready to define everything we need for training our Seq2Seq model
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

load_model = True
save_model = True

# Model hyperparameters
src_vocab_size = len(pli.vocab)
trg_vocab_size = len(ktl.vocab)
embedding_size = 512
num_heads = 8
num_encoder_layers = 6
num_decoder_layers = 6
dropout = 0.10
max_len = 100
forward_expansion = 4
src_pad_idx = ktl.vocab.stoi["<pad>"]

# Tensorboard to get nice loss plot
writer = SummaryWriter("runs/loss_plot")
step = 0

train_iterator, test_iterator = BucketIterator.splits(
    (train, test),
    batch_size=batch_size,
    sort_within_batch=True,
    sort_key=lambda x: len(x.p),
    device=device,
)
model = Transformer(
    embedding_size,
    src_vocab_size,
    trg_vocab_size,
    src_pad_idx,
    num_heads,
    num_encoder_layers,
    num_decoder_layers,
    forward_expansion,
    dropout,
    max_len,
    device,
).to(device)

optimizer = optim.Adam(model.parameters(), lr=learning_rate)

scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(
    optimizer, factor=0.1, patience=10, verbose=True
)

pad_idx = ktl.vocab.stoi["<pad>"]
criterion = nn.CrossEntropyLoss(ignore_index=pad_idx)

if __name__ == '__main__':

    # training loop
    if sys.argv[1] == "-train":
        for epoch in range(num_epochs):
            model.eval()
            # little bit of output to check the progress
            if epoch % 100 == 0:
                print(f"[Epoch {epoch} / {num_epochs}]")

                sentences = [
                    {'pli': ['PROCEDURE', 'MAIN', '{{type0}}', '{{type1}}'],
                     'context': {'type0': 'Array', 'type1': 'String'}},
                    {'pli': ['DO'], 'context': {}},
                    {'pli': ['END'], 'context': {}}
                ]
                print(f"Translated example sentence:")
                level = 0
                for s in sentences:
                    translated = translate_sequence(
                        s['pli'], pli, ktl, device, max_length=50
                    )
                    transpiled, level = transpile_sequence({
                        'code': translated,
                        'context': s['context']
                    }, level)
                    print(f"{transpiled}")
            model.train()
            losses = []

            for batch_idx, batch in enumerate(train_iterator):
                # Get input and targets and get to cuda
                inp_data = batch.p.to(device)
                target = batch.k.to(device)

                # Forward
                output = model(inp_data, target[:-1, :])

                output = output.reshape(-1, output.shape[2])
                target = target[1:].reshape(-1)

                optimizer.zero_grad()

                loss = criterion(output, target)
                losses.append(loss.item())

                # Back prop
                loss.backward()
                # Clip to avoid exploding gradient issues, makes sure grads are
                # within a healthy range
                torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1)

                # Gradient descent step
                optimizer.step()

                # plot to tensorboard
                writer.add_scalar("Training loss", loss, global_step=step)
                step += 1

            mean_loss = sum(losses) / len(losses)
            scheduler.step(mean_loss)

        if save_model:
            checkpoint = {
                "state_dict": model.state_dict(),
                "optimizer": optimizer.state_dict(),
            }
            save_checkpoint(checkpoint)


    elif sys.argv[1] == "-run":
        load_checkpoint(torch.load("checkpoint.pth.tar"), model, optimizer)
        # Lexer setup
        input_stream = FileStream(sys.argv[2])
        lexer = PLILexer(input_stream)
        stream = CommonTokenStream(lexer)

        # Parser setup
        parser = PLIParser(stream)
        tree = parser.program()

        # Dataset generation
        visitor = PLIVisitor()
        statements = visitor.visit(tree)

        #for s in statements:
        #    print(s)

        level = 0
        for s in statements:
            translated = translate_sequence(
                s["pli"], pli, ktl, device, max_length=50
            )
            transpiled, level = transpile_sequence({
                'code': translated,
                'context': s['context']
            }, level)
            print(f"{transpiled}")
    else:
        print("usage:"
              "\n\tpli2kt -train dataset-file to train the transformer"
              "\n\tpli2kt -run source-file to transpiler the source file")
