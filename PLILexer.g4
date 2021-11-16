
lexer grammar PLILexer;
PAD                     : '#' ; /*Special */
QUOTE                   : '\'';
COLON                   : ':' ;
DOT                     : '.' ;
COMMA                   : ',' ;
SEMICOLON               : ';' ;
OPEN_PAREN              : '(' ;
CLOSE_PAREN             : ')' ;
PLUS                    : '+' ;
MINUS                   : '-' ;
SLASH                   : '/' ;
STAR                    : '*' ;
PERCENT                 : '%' ;
EQUAL                   : '=' ;
STARSTAR                : '**';
PLUSEQUAL               : '+=';
MINUSEQUAL              : '-=';
STAREQUAL               : '*=';
SLASHEQUAL              : '/=';
CONCAT                  : '||' | '!!';
EQ                      : E Q | EQUAL ;
NE                      : [\u00AA] '=' | [\uFFFD] '=' | '<>' | '^=' | '~=' | '¬=';
GT                      : G T | '>' ;
LT                      : L T | '<' ;
GE                      : G E | '>=';
LE                      : L E | '<=';
AND                     : '&' ;
OR                      : '|' | '!';
NOT                     : [\u00AA] | [\uFFFD] | '^' | '~' | '¬';

ABNORMAL                : A B N O R M A L;
ACTIVATE                : A C T I V A T E;
ADDBUFF                 : A D D B U F F;
ALIAS                   : A L I A S;
ALIGNED                 : A L I G N E D;
ALLOCATE                : A L L O C A T E;
ANYCONDITION            : A N Y C O N D I T I O N;
AREA                    : A R E A;
ASCII                   : A S C I I;
ASSIGNABLE              : A S S I G N A B L E;
ASSEMBLER               : A S S E M B L E R;
ASM                     : A S M;
ATTACH                  : A T T A C H;
ATTENTION               : A T T E N T I O N;
AUTOMATIC               : A U T O M A T I C | A U T O;
B1                      : B [1];
B2                      : B [2];
B3                      : B [3];
B4                      : B [4];
BACKWARDS               : B A C K W A R D S;
BASED                   : B A S E D;
BEGIN_                  : B E G I N;
BIGENDIAN               : B I G E N  D I A N;
BINARY                  : B I N (A R Y)?;
BIT                     : B I T;
BKWD                    : B K W D;
BLKSIZE                 : B L K S I Z E;
BUFFERED                : B U F F E R E D;
BUFFERS                 : B U F F E R S;
BUFFOFF                 : B U F F O F F;
BUFND                   : B U F N D;
BUFNI                   : B U F N I;
BUFSP                   : B U F S P;
BUILTIN                 : B U I L T I N;
BY                      : B Y;
BYADDR		            : B Y A D D R;
BYVALUE		            : B Y V A L U E;
BX		                : B X;
CALL                    : C A L L;
CDECL                   : C D E C L;
CELL                    : C E L L;
CHARACTER               : C H A R (A C T E R)?;
CHARGRAPHIC             : C H A R G R  A P H I C;
CHECK                   : C H E C K;
CLOSE                   : C L O S E;
COBOL                   : C O B O L;
COLUMN                  : C O L U M N;
COMPLEX                 : C O M P L E X;
CONNECTED               : C O N N E C T E D | C O N N;
CONDITION               : C O N D I T I O N | C O N D;
CONSECUTIVE             : C O N S E C U T I V E;
CONSTANT                : C O N S T A N T | C O N S T;
CTLASA                  : C T L A S A;
CTL360                  : [cC] [tT] [lL] [3] [6] [0];
CONTROLLED              : C O N T R O L L E D;
CONVERSION              : C O N V E R S I O N  | C O N V ;
COPY                    : C O P Y;
DB                      : D B;
DATA                    : D A T A;
DATE                    : D A T E;
DECLARE                 : D E C L A R E | D C L;
DEACTIVATE              : D E A C T I V A T E;
DECIMAL                 : D E C (I M A L)?;
DEFAULT                 : D E F A U L T | D F T;	// specialKeyWord(DEFAULT,DEFAULT,VARNAME);
DELAY		            : D E L A Y;
DELETE		            : D E L E T E;
DEFINE		            : D E F I N E;
DEFINED	                : D E F (I N E D)?;
DESCRIPTOR	            : D E S C R I P T O R;
DESCRIPTORS	            : D E S C R I P T O R S;
DETACH		            : D E T A C H;
DIMACROSS               : D I M A C R O S S; //TODO
DIMENSION	            : D I M E N S I O N | D I M;
DIRECT		            : D I R E C T;
DISPLAY		            : D I S P L A Y;
DO	 	                : D O;
DOWNTHRU	            : D O W N T H R U;
EDIT	 	            : E D I T ;
ELSE		            : E L S E;
END                     : E N D;
ENDFILE		            : E N D F I L E;
ENDPAGE		            : E N D P A G E;
ENTRY                   : E N T R Y;
ENVIRONMENT             : E N V I R O N M E N T | E N V;
ERROR                   : E R R O R;
EVENT                   : E V E N T;
EXCLUSIVE               : E X C L U S I V E | E X C L;
EXIT                    : E X I T;
EXPORTS                 : E X P O R T S;
EXTERNAL                : E X T E R N A L | E X T;
FB                      : F B;
FS                      : F S;
FBS                     : F B S;
FETCH                   : F E T C H;
FETCHABLE               : F E T C H A B L E;
FILE_                   : F I L E;
FINISH                  : F I N I S H;
FIXED                   : F I X E D;
FIXEDOVERFLOW           : F I X E D O V E R F L O W;
FLOAT                   : F L O A T;
FLUSH                   : F L U S H;
FREE                    : F R E E;
FORCE                   : F O R C E; //TODO
FOREVER                 : F O R E V E R;
FORTRAN                 : F O R T R A N;
FORMAT	                : F O R M A T;
FROM                    : F R O M;
FROMALIEN               : F R O M A L I E N;
GENERIC                 : G E N E R I C;
GENKEY                  : G E N K E Y;
GET                     : G E T;
GO                      : G O;
GOTO                    : G O T O;
GRAPHIC                 : G R A P H I C;
GX                      : G X;
HANDLE		            : H A N D L E;
HEXADEC		            : H E X A D E C;
IEEE		            : I E E E;
IF                      : I F;
IGNORE                  : I G N O R E;
IMPORTED                : I M P O R T E D;
IN                      : I N;
INCLUDE                 : '%' I N C L U D E; // TODO preprocessor
INDEXAREA               : I N D E X A R E A;
INDEXED                 : I N D E X E D;
INDFOR                  : I N D F O R; //TODO
INITIAL_                : I N I T (I A L)?;
INLINE                  : I N L I N E;
INONLY                  : I N O N L Y; //TODO
INOUT                   : I N O U T; //TODO
INPUT                   : I N P U T;
INTER                   : I N T E R;
INTERACTIVE             : I N T E R A C T I V E;
INTERNAL                : I N T E R N A L | I N T;
INTO                    : I N T O;
INVALIDOP               : I N V A L I D O P;
IRREDUCIBLE             : I R R E D U C I B L E;
ITERATE		            : I T E R A T E;
KEY                     : K E Y;
KEYED                   : K E Y E D;
KEYFROM                 : K E Y F R O M;
KEYLENGTH               : K E Y L E N G T H;
KEYLOC                  : K E Y L O C;
KEYTO                   : K E Y T O;
LABEL                   : L A B E L;
LEAVE                   : L E A V E ;
LIMITED                 : L I M I T E D;
LIKE                    : L I K E;
LINE                    : L I N E;
LINESIZE                : L I N E S I Z E;
LINKAGE                 : L I N K A G E;
LIST                    : L I S T;
LITTLEENDIAN	        : L I T T L E E N D I A N;
LOCAL                   : L O C A L;
LOCATE                  : L O C A T E;
LOOP                    : L O O P;
MAIN                    : M A I N;
NAME                    : N A M E;
NCP                     : N C P;
NOCHARGRAPHIC           : N O C H A R G R A P H I C;
NOCHECK                 : N O C H E C K;
NOCONVERSION            : N O C O N V E R S I O N;
NODESCRIPTOR            : N O D E S C R I P T O R;
NOEXECOPS               : N O E X E C O P S;
NOFIXEDOVERFLOW         : N O F I X E D O V E R F L O W;
NOINIT                  : N O I N I T;
NOINLINE                : N O I N L I N E;
NOINVALIDOP             : N O I N V A L I D O P;
NOLOCK                  : N O L O C K;
NONASSIGNABLE           : N O N A S S I G N A B L E;
NONCONNECTED            : N O N C O N N E C T E D;
NONE                    : N O N E ;
NONVARYING	            : N O N V A R Y I N G;
NON_QUICK               : 'NON_QUICK';
NO_QUICK_BLOCKS	        : 'NO_QUICK_BLOCKS';
NOOVERFLOW              : N O O V E R F L O W;
NOPRINT		            : N O P R I N T;
NORMAL		            : N O R M A L;
NOSIZE                  : N O S I Z E;
NOSUBSCRIPTRANGE        : N O S U B S C R I P T R A N G E;
NOSTRINGRANGE           : N O S T R I N G R A N G E;
NOSTRINGSIZE            : N O S T R I N G S I Z E;
NOTE      	            : N O T E;
NOUNDERFLOW             : N O U N D E R F L O W;
NOWRITE                 : N O W R I T E;
NOZERODIVIDE            : N O Z E R O D I V I D E;
NULLINIT                : N U L L I N I T;//TODO
OFFSET                  : O F F S E T;
ON                      : O N;
OPEN                    : O P E N ;
OPTIONAL                : O P T I O N A L;
OPTIONS                 : O P T I O N S;
OPTLINK                 : O P T L I N K;
ORDER                   : O R D E R;
ORDINAL                 : O R D I N A L;
OTHERWISE	            : O T H E R (W I S E)?;
OUTONLY                 : O U T O N L Y;
OUTPUT		            : O U T P U T;
OVERFLOW	            : O V E R F L O W;
PACKAGE                 : P A C K A G E;
PACKED_DECIMAL  : 'PACKED_DECIMAL';
PACKED                  : P A C K E D;
PAGE                    : P A G E;
PAGESIZE                : P A G E S I Z E;
PARAMETER               : P A R A M E T E R;
PASSWORD	            : P A S S W O R D;
PENDING		            : P E N D I N G;
PICTURE	                : P I C (T U R E)?;
POINTER	                : P O I N T E R | P T R;
POSITION	            : P O S (I T I O N)?;
PRECISION	            : P R E C I S I O N;
PRINT	                : P R I N T;
PRIORITY                : P R I O R I T Y;
PROCEDURE	            : P R O C E D U R E | P R O C;
PUT                     : P U T;
RANGE                   : R A N G E;
READ                    : R E A D;
REAL                    : R E A L;
RECORD                  : R E C O R D;
RECSIZE                 : R E C S I Z E;
RECURSIVE               : R E C U R S I V E;
REDUCIBLE	            : R E D U C I B L E;
REENTRANT               : R E E N T R A N T;
REFER                   : R E F E R;
REGIONAL                : R E G I O N A L;
RELEASE                 : R E L E A S E;
RENAME                  : R E N A M E;
REORDER                 : R E O R D E R;
REPEAT                  : R E P E A T;
REPLACE                 : R E P L A C E;
REPLY		            : R E P L Y;
REREAD		            : R E R E A D;
RESERVED	            : R E S E R V E D;
RESERVES	            : R E S E R V E S;
RESIGNAL	            : R E S I G N A L;
RETCODE		            : R E T C O D E;
RETURN		            : R E T U R N;
RETURNS		            : R E T U R N S;
REUSE		            : R E U S E;
REVERT		            : R E V E R T;
REWRITE		            : R E W R I T E;
SCALARVARYING	        : S C A L A R V A R Y I N G;
SELECT		            : S E L E C T;
SEPARATE_STATIC	: 'SEPARATE_STATIC';
SET                     : S E T;
SEQUENTIAL	            : S E Q U E N T I A L;
SIGNAL                  : S I G N A L;
SIGNED                  : S I G N E D;
SIS                     : S I S;
SIZE                    : S I Z E;
SKIP_                   : S K I P;
SNAP	                : S N A P; //     	specialKeyWord(SNAP,SNAP,VARNAME);
STATIC		            : S T A T I C;
STDCALL		            : S T D C A L L;
STORAGE		            : S T O R A G E;
STOP		            : S T O P;
STREAM		            : S T R E A M;
STRING	 	            : S T R I N G;
STRINGRANGE             : S T R I N G R A N G E;
STRINGSIZE		        : S T R I N G S I Z E;
STRINGVALUE	            : S T R I N G V A L U E;
STRUCTURE	            : S T R U C T U R E;
SUB                     : S U B;
SUBSCRIPTRANGE	        : S U B S C R I P T R A N G E;
SUPPRESS                : S U P P R E S S; //TODO
SUPPORT		            : S U P P O R T;
SYSTEM		            : S Y S T E M;
SYSIN                   : S Y S I N;
SYSOUT                  : S Y S O U T;
SYSERR                  : S Y S E R R;
TASK		            : T A S K;
THEN		            : T H E N;
THREAD		            : T H R E A D;
TITLE		            : T I T L E;
TO                      : T O;
TOTAL                   : T O T A L;
TP                      : T P;
TRANSIENT               : T R A N S I E N T;
TRANSMIT                : T R A N S M I T;
TRKOFL                  : T R K O F L;
TSTACK                  : T S T A C K;
TYPE                    : T Y P E;
UNALIGNED               : U N A L (I G N E D)?;
UNBUFFERED              : U N B U F (F E R E D)?;
UNCONNECTED             : U N C O N N E C T E D;
UNDEFINEDFILE           : U N D E F I N E D F I L E;
UNDERFLOW_              : U N D E R F L O W;
UNION                   : U N I O N;
UNLOCK                  : U N L O C K;
UNSIGNED                : U N S I G N E D;
UNTIL                   : U N T I L;
UPDATE                  : U P D A T E;
UPTHRU                  : U P T H R U;
VALIDATE                : V A L I D A T E;
VALUE                   : V A L U E;
VALUELIST               : V A L U E L I S T; //TODO
VALUELISTFROM           : V A L U E L I S T F R O M; //TODO
VALUERANGE              : V A L U E R A N G E; //TODO
VARIABLE                : V A R I A B L E;
VARYING                 : V A R (Y I N G)?;
VARYINGZ                : V A R Y I N G Z;
VB                      : V B;
VBS                     : V B S;
VS                      : V S;
VSAM                    : V S A M;
WAIT                    : W A I T;
WHEN                    : W H E N;
WIDECHAR                : W I D E C H A R;
WINMAIN                 : W I N M A I N;
WHILE                   : W H I L E;
WRITE                   : W R I T E;
WX                      : W X;
XN                      : X N;
XU                      : X U;
ZERODIVIDE              : Z E R O D I V I D E;

EXEC                    : E X E C; // SQL preprocessor
SQL                     : S Q L; // SQL preprocessor


IDENTIFIER              : ( [_$#@]+ | [a-zA-Z]+) ( [_$#@]+ | [a-zA-Z]+ | [0-9])*
                        ;


INTEGER_LITERAL         : [0-9] [0-9_]*
                        ;

DECIMAL_LITERAL         :   [0-9] [0-9_]* '.' [0-9] [0-9_]*
                        |   [0-9] [0-9_]*'.'
                        |   '.' [0-9] [0-9_]*
                        ;

FLOAT_LITERAL           : INTEGER_LITERAL   E ( '-' | '+' )? [0-9] ( [0-9] )?
                        | DECIMAL_LITERAL   E ( '-' | '+' )? [0-9] ( [0-9] )?
                        ;

BIT_LITERAL             :   ( '\'' (  '0' | '1' | '_' )+ '\'' | '"' (  '0' | '1' | '_' )+ '"' )( B )
                        ;

HEX_LITERAL             :   ( '\'' ( [a-fA-F0-9_] )+ '\'' | '"' ( [a-fA-F0-9_] )+ '"' )( X )
                        ;

XNHEX_LITERAL           :   ( '\'' ( [a-fA-F0-9_] )+ '\'' | '"' ( [a-fA-F0-9_] )+ '"' )( XN )
                        ;

XUHEX_LITERAL           :   ( '\'' ( [a-fA-F0-9_] )+ '\'' | '"' ( [a-fA-F0-9_] )+ '"' )( XU )
                        ;

B4HEX_LITERAL           :   ( '\'' ( [a-fA-F0-9_] )+ '\'' | '"' ( [a-fA-F0-9_] )+ '"' )( B4 | BX )
                        ;

B3HEX_LITERAL           :   ( '\'' ( [0-7_] )+ '\'' | '"' ( [0-7_] )+ '"' )( B3 )
                        ;

/* A CHARACTER constant is a contiguous sequence of characters enclosed in single or double quotation marks.*/
STRING_LITERAL          : ('"' (~["\\])* '"'
                        | '\'' ('\'\'' | ~['\\])* '\'')
                        ;
ASTRING_LITERAL         : ('"' (~["\\])* '"' | '\'' (~['\\])* '\'')( A )
                        ;
ESTRING_LITERAL         : ('"' (~["\\])* '"' | '\'' (~['\\])* '\'')( E )
                        ;
//P_FORMAT                : P '\'' ('\'\'' | ~['\\])* '\''
//                        ;


COMMENT                 : '/*' .*? '*/' -> channel(HIDDEN)
                        ;
WS                      :   [ \r\t\u000C\n]+ -> skip
                        ;

INJECT                  :   '/#' .*? '#/'
                        ;

fragment A:('a'|'A');
fragment B:('b'|'B');
fragment C:('c'|'C');
fragment D:('d'|'D');
fragment E:('e'|'E');
fragment F:('f'|'F');
fragment G:('g'|'G');
fragment H:('h'|'H');
fragment I:('i'|'I');
fragment J:('j'|'J');
fragment K:('k'|'K');
fragment L:('l'|'L');
fragment M:('m'|'M');
fragment N:('n'|'N');
fragment O:('o'|'O');
fragment P:('p'|'P');
fragment Q:('q'|'Q');
fragment R:('r'|'R');
fragment S:('s'|'S');
fragment T:('t'|'T');
fragment U:('u'|'U');
fragment V:('v'|'V');
fragment W:('w'|'W');
fragment X:('x'|'X');
fragment Y:('y'|'Y');
fragment Z:('z'|'Z');