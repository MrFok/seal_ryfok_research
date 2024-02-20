import sys
from antlr4 import *
from JSON5Lexer import JSON5Lexer
from JSON5Parser import JSON5Parser
from CFDataValid import CFDataValid
from g4Refine import g4Refine

import io
import sys

import subprocess

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
    # main(sys.argv)
    # try:
    #     output = subprocess.check_output(['cfn-lint', '--ignore-bad-template', '--non-zero-exit-code', 'informational',  sys.argv[1]])
    #     # print(output.decode())
    # except subprocess.CalledProcessError as e:
    #     # print(f'cfn-lint output: "{e.output.decode()}"')
    #     errors = e.output.decode().splitlines()
    #     for i, error in enumerate(errors):
    #         print(f"{i} - {error}")  

    # validator = CFDataValid()
    # validator.validate_file(sys.argv[1], verbose=False)
    # print("Get Leaf")
    # leafs = validator.get_leaf_nodes()
    # for i, leaf in enumerate(leafs):
    #     print(f"{i + 1}: {leaf}")
    # ds1, ds2, pass1, pass2 = validator.validate_parser(verbose=True)

    refiner = g4Refine(sys.argv[1])






