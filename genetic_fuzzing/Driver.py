import sys
from antlr4 import *
from JSON5Lexer import JSON5Lexer
from JSON5Parser import JSON5Parser
from CFDataValid import CFDataValid
from JSON5Listener import JSON5Listener
from g4Refine import g4Refine
# from regex_engine.main import converRegToEr
from grammarinator import *

import io
import sys

import pickle
import json
import regex as re
from regexify import PatternTrie

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

def traverse_antlr_pre_order(dictionary, prefix = "", verbose=False, item_dict = {}):
        """
        Traverse tree JSON in pre-order fashion

        :param dictionary: The dictionary to traverse
        :param prefix: The prefix to add to the keys
        :param verbose: Whether to print the key-value pairs
        :return: item_dict: The dictionary with the key-value pairs
        """

        for key, value in dictionary.items():
            if prefix != "":
                key = prefix + "." + key 
            if not isinstance(value, (dict, list)):
                print(f"Key: {key} | Value: {value}")  # Or perform any other operation on the key-value pair
                item_dict[key] = value
            elif isinstance(value, dict):
                traverse_antlr_pre_order(value, key, item_dict)
            elif isinstance(value, list):
                validator = CFDataValid()
                templates = validator.extract_templates(value)
                item_dict[key] = templates[0]
                
                # Regexify
                # trie = PatternTrie(*value)
                # print(trie.pattern)
                # item_dict[key] = re.compile(trie.pattern)
                # print(f"List Add: {key} | {item_dict[key]}")
                # p = re.compile(r"\L<words>", words=value).pattern
        return item_dict

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

    validator = CFDataValid()

    # input_stream = FileStream("testJSON.json5")
    # lexer = JSON5Lexer(input_stream)
    # stream = CommonTokenStream(lexer)
    # parser = JSON5Parser(stream)
    
    # tree = parser.json5()

    # walker = ParseTreeWalker()
    # listener = JSON5Listener()
    # walker.walk(listener, tree)   

    ### Pickle Demo
    # testJSON.38b22e6ec86247f68bbf63c4497f0004.grt
    # DataPipeline-multiple-StringValue.c132e674b6714125ad908acf18204b21.grt\

    # SET GRAMMAR FILE TO PARSE
    # parse_file = 'testJSON.json5'
    # grammar_file = 'JSON5.g4'
    # result = subprocess.run('grammarinator-parse ' + grammar_file + ' -r json5 -i ' + parse_file, capture_output=True, text=True, shell=True)
    # generated_file = result.stdout.strip()
    # print(generated_file)
    # file = open('testJSON.3aede06d0dd74faca46a90826369f088.grt', 'rb')
    # pickle_file = pickle.load(file) 
    # # pickle_file.print()
    # dict_format_pickle_file = pickle_file.__str__()
    # pickle_file_dict = json.loads(dict_format_pickle_file)
    # print(json.dumps(pickle_file_dict, indent=3))
    # print("\n\n")

    # function_dict = traverse_antlr_pre_order(pickle_file_dict, verbose=False)
    # print(function_dict)
    
    # test_list = ['Property', 'io.file.table.size', 'io.file.buffer.size', 'io.input.buffer.size']
    # templates = validator.extract_templates(test_list)
    # print(templates[2])

    refine = g4Refine()
    refine.refine_demo_2()
    # refine.specialize("testJSON.json5", verbose=True)
    # new_pair, key_parser_rule, value_parser_rule, new_lexer_key, new_lexer_value = refine.submit_change("AllowedValues", "test")
    # PickleTreeCodec.decode_annotated(pickle_file)

    




