import sys
from antlr4 import *
from JSON5Lexer import JSON5Lexer
from JSON5Parser import JSON5Parser

import io
import sys

def main(argv):
    passFailStr = "PASS" if isValidCF(argv[1], verbose=False) else "FAIL"
    print(argv[1] + " | " + passFailStr)

def isValidCF(filePath, verbose=False):
    parsedStatus = True # True if parsed successfully, False otherwise
    input_stream = FileStream(filePath)
    lexer = JSON5Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = JSON5Parser(stream)

    # Redirect stdout and stderr to buffer
    old_stderr = sys.stderr
    old_strout = sys.stdout
    strerr_buffer = io.StringIO()
    strout_buffer = io.StringIO()
    sys.stderr = strerr_buffer
    sys.stdout = strout_buffer

    tree = parser.json5()

    # Restore stdout & stderr
    sys.stdout = old_stderr
    statements = strerr_buffer.getvalue() + strout_buffer.getvalue()
    
    if verbose:
        # print(tree.toString())
        print(f'Stdout + Stderr output: "{statements}"')

    return True if statements == "" else False

if __name__ == '__main__':
    main(sys.argv)







