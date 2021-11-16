parser grammar PLIParser;

options {   tokenVocab = PLILexer; }

program                     : (stmt)* EOF
                            ;

stmt                        : label? statement
                            ;

comment                     : COMMENT
                            ;

label                       : IDENTIFIER COLON?
                            ;


statement                   :   procedureStmt
                            |   declareStmt
                            |   assignStmt
                            |   callStmt
                            |   returnStmt
                            |   ifStmt
                            |   comment
                            |   nopStmt
                            ;

nopStmt                     : SEMICOLON;

assignStmt                  : identifier (COMMA identifier)* EQUAL expression assignByName? SEMICOLON
                            | identifier (COMMA identifier)* PLUSEQUAL expression assignByName? SEMICOLON
                            | identifier (COMMA identifier)* MINUSEQUAL expression assignByName? SEMICOLON
                            | identifier (COMMA identifier)* STAREQUAL  expression assignByName? SEMICOLON
                            | identifier (COMMA identifier)* SLASHEQUAL expression assignByName? SEMICOLON
                            ;

assignByName                : (COMMA BY NAME)
                            ;

declareStmt                 : DECLARE declaration (COMMA declaration)*   SEMICOLON
                            | DECLARE OPEN_PAREN declaration (COMMA declaration)*  CLOSE_PAREN  SEMICOLON
                            ;

declaration                 : level? name (attributes)*
                            | name TYPE identifier VALUE OPEN_PAREN expression CLOSE_PAREN
                            ;

level                       : INTEGER_LITERAL
                            ;

name                        : identifier
                            | OPEN_PAREN factoredNames CLOSE_PAREN
                            | STAR
                            ;

factoredNames               : identifier (COMMA identifier)*
                            ;

attributes                  : data
                            | alignment
                            | scope
                            | storage
                            //| complementary
                            | constant
                            | initialization
                            ;


data                        : BINARY        (OPEN_PAREN precision  CLOSE_PAREN)?
                            | DECIMAL       (OPEN_PAREN precision  CLOSE_PAREN)?
                            | FLOAT         (OPEN_PAREN precision  CLOSE_PAREN)?
                            | CHARACTER     (OPEN_PAREN expression CLOSE_PAREN)? (VARYING? | VARYINGZ?)
                            | CHARACTER     (OPEN_PAREN STAR CLOSE_PAREN)?
                            | FIXED         (OPEN_PAREN precision  CLOSE_PAREN)?
                            | PICTURE       expression
                            | POINTER
                            | BIT           (OPEN_PAREN expression CLOSE_PAREN)? (VARYING? | VARYINGZ?)
                            | BUILTIN
                            | BASED         (OPEN_PAREN expression CLOSE_PAREN)
                            | CONNECTED
                            | FILE_
                            | RECORD
                            | PRINT
                            | SEQUENTIAL
                            | VARIABLE
                            | INPUT
                            | STREAM
                            | OUTPUT
                            | UPDATE
                            | DIRECT
                            | BUFFERED
                            | UNBUFFERED
                            | SYSIN
                            | SYSOUT
                            | SYSERR
                            | KEYED
                            | LIKE          like=identifier
                            | LABEL
                            | CONDITION
                            //TODO add more types
                            ;

precision                   : INTEGER_LITERAL (COMMA decimals)?
                            ;

decimals                    : INTEGER_LITERAL
                            ;


alignment                   : ALIGNED
                            | UNALIGNED
                            ;

scope                       : INTERNAL
                            | EXTERNAL
                            | EXTERNAL OPEN_PAREN externalName CLOSE_PAREN
                            | ENVIRONMENT OPEN_PAREN VSAM? externalName CLOSE_PAREN
                            | RESERVED
                            ;
externalName                : STRING_LITERAL
                            | GENKEY
                            ;

storage                     : STATIC
                            | AUTOMATIC
                            | BASED (OPEN_PAREN locator CLOSE_PAREN)?
                            | DEFINED locator (POSITION OPEN_PAREN expression CLOSE_PAREN)?
                            | CONTROLLED
                            ;

locator                     : expression
                            ;


constant                    : VALUE OPEN_PAREN expression CLOSE_PAREN
                            ;

initialization              : INITIAL_ OPEN_PAREN initValue (COMMA initValue)* CLOSE_PAREN
                            | INITIAL_ callStmt
                            | INITIAL_ TO OPEN_PAREN initSpec CLOSE_PAREN OPEN_PAREN expression (COMMA expression)* CLOSE_PAREN
                            ;

initSpec                    : VARYING
                            | VARYINGZ
                            | NONVARYING
                            ;

initValue                   : repetitionFactor? expression
                            ;

ifStmt                      :   IF expression THEN stmt
                            ;

callStmt                    : CALL IDENTIFIER (OPEN_PAREN (expression)* CLOSE_PAREN)? SEMICOLON
                            | CALL IDENTIFIER (OPEN_PAREN expression (COMMA expression)* CLOSE_PAREN)? SEMICOLON
                            ;

returnStmt                  : RETURN (OPEN_PAREN expression CLOSE_PAREN)? SEMICOLON
                            ;

procedureStmt               : PROCEDURE (OPEN_PAREN procedureParams CLOSE_PAREN)?
                                        (OPTIONS OPEN_PAREN procedureOptions CLOSE_PAREN)?
                                        (RETURNS OPEN_PAREN procedureReturns CLOSE_PAREN)? REORDER? SEMICOLON
                              (stmt)*
                              END (identifier)? SEMICOLON
                            ;

procedureParams             : procedureParam  (COMMA procedureParam)*
                            ;

procedureParam              : IDENTIFIER
                            ;

procedureOptions            : procedureOption  (COMMA? procedureOption)*
                            ;


procedureOption             : MAIN
                            | REENTRANT
                            | RECURSIVE
                            | COBOL
                            | ASM
                            | INTER
                            ;

procedureReturns            : (attributes)*
                            ;


expression                  : literal
                            | identifier
                            | (NOT | PLUS | MINUS) expression
                            | expression STARSTAR expression
                            | expression (STAR | SLASH | PERCENT) expression
                            | expression (PLUS | MINUS | CONCAT) expression
                            | expression comparison expression
                            | expression EQUAL expression
                            | expression (AND | OR) expression
                            | CALL (expression)*
                            | OPEN_PAREN expression CLOSE_PAREN
                            ;

comparison                  :   (NE | GT | LT | GE | LE )
                            ;

literal                     : repetitionFactor? INTEGER_LITERAL
                            | DECIMAL_LITERAL
                            | FLOAT_LITERAL
                            | HEX_LITERAL
                            | repetitionFactor?  STRING_LITERAL
                            | repetitionFactor?  BIT_LITERAL
                            //| P_FORMAT
                            ;

repetitionFactor            : (OPEN_PAREN repeater=expression CLOSE_PAREN)
                            ;

identifier                  : simpleIdentifier
                            | identifier DOT member
                            | identifier OPEN_PAREN subscript? (COMMA subscript)* CLOSE_PAREN
                            | identifier picture
                            ;

simpleIdentifier            : IDENTIFIER
                            /* Keywords */
                            | (MAIN
                            | TITLE
                            | FIXED
                            | COPY
                            | FROM
                            | REPLY
                            | CONDITION
                            | KEY
                            | DATE
                            | PAGE
                            | DATA
                            | OPEN
                            | IN
                            | SYSTEM
                            | NAME
                            | VALUE
                            | OFFSET
                            | PAGESIZE
                            | LINESIZE
                            | RESERVED
                            | NOTE
                            | STRING
                            | SYSIN
                            | RECORD
                            | ERROR)
                            ;

member                      : identifier
                            ;

subscript                   : expression
                            ;

picture                     : STRING_LITERAL
                            ;
