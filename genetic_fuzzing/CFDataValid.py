import io
import sys
from antlr4 import *
from JSON5Lexer import JSON5Lexer
from JSON5Parser import JSON5Parser
from JSON5Visitor import JSON5Visitor

import subprocess

CF_FILES = {"DataPipeline-multiple-StringValue.json", 
            "DirectoryServiceSimpleAD.json",
            "DMSAuroraToS3FullLoadAndOngoingReplication.json",
            "EMRClusterGangliaWithSparkOrS3backedHbase.json",
            "EMRClusterWithAdditioanalSecurityGroups.json",
            "NetworkLoadBalancerWithEIPs.json",
            "SingleENIwithMultipleEIPs.json",
            "SNSTopic.json",
            "SQSFIFOQueue.json",
            "SQSStandardQueue.json"
            }

NON_CF_FILES = {"BackgroundMediaPlayback.json",
                "GoogleDataFeed.json",
                "MapsMarker.json",
                "NASAMarsWeather.json",
                "OneSkyJasonSample2.json",
                "OpenAIPetStoreSimple.json",
                "RiotClientInstalls.json",
                "RoboMakerOneBedroom.json",
                "ShopifySectionData.json",
                "SolarEnergeticParticle.json"
                }

INVALID_ROOTS = {}
#":", "}", "{", ","

CF_FILES_DIR = "cf_json\\"
NON_CF_FILES_DIR = "non_cf_json\\"
GRAMMAR_BUILD_PATH = "build.sh"

"""
Create a CFDataValid class to validate current JSON5 implementation
"""
class CFDataValid():
    def __init__(self):
        self.cf_files = CF_FILES
        self.non_cf_files = NON_CF_FILES
        self.cf_states = {}
        self.non_cf_states = {}
        self.curr_tree = None

    def validate_file(self, filePath, verbose=False):
        """
        Validates given file if it is a valid JSON and a valid CloudFormation template.

        Args:
            filePath (str): The path to the JSON5 file.
            verbose (bool, optional): If True, prints additional information. Defaults to False.

        Returns:
            bool: True if the file is parsed successfully, False otherwise.
        """
        if verbose:
            print(f'Validating file: "{filePath}"')
        input_stream = FileStream(filePath)
        lexer = JSON5Lexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = JSON5Parser(stream)

        # Redirect stdout and stderr to buffer
        old_stderr = sys.stderr
        old_stdout = sys.stdout
        strerr_buffer = io.StringIO()
        strout_buffer = io.StringIO()
        sys.stderr = strerr_buffer
        sys.stdout = strout_buffer

        tree = parser.json5()
        self.curr_tree = tree

        # Restore stdout & stderr
        sys.stdout = old_stdout
        sys.stderr = old_stderr
        statements = strerr_buffer.getvalue() + strout_buffer.getvalue()
        # print(f"Tokens: {tree.toStringTree(recog=parser)}")
        # print(tree.getChildCount())
        # visitTree = JSON5Visitor().visit(tree)
        # print(visitTree)
        # Check if file was parsed successfully via JSON5.g4 grammar
        if statements != "":
            if verbose:
                print("JSON5 Validation | FAIL")
            return False

        if verbose:
            print("JSON5 Validation | PASS")
        return True

    def cf_validate(self, filePath, verbose=False):
        """
        Validates file adherance to CloudFormation template using cfn-lint.

        cfn-lint runs with .cfnlintrc configuration file in the root directory.

        Args:
            filePath (str): The path to the CloudFormation template file.
            verbose (bool, optional): If True, prints additional information about the validation process. Defaults to False.

        Raises:
            Exception: If the file is not a valid CloudFormation template.

        Returns:
            None
        """

        try:
            subprocess.check_output(['cfn-lint', filePath])
        except subprocess.CalledProcessError as e:
            if verbose:
                print(f'cfn-lint Validation | FAIL')
                print(f'cfn-lint output: "{e.output.decode()}"')
            return False

        if verbose:
            print(f'cfn-lint Validation | PASS')
        return True
    
    def validate_parser(self, verbose=False):
        """
        Validates if the grammar is parsing our test CF files and non-CF files correctly.

        Args:
            verbose (bool): If True, prints the validation status for each file.

        Returns:
            dict: A dictionary of the validation status for each CF file.
            dict: A dictionary of the validation status for each non-CF file.
            int: The number of CF files that passed validation.
            int: The number of non-CF files that passed validation
        """

        cf_pass = 0
        non_cf_pass = 0
        if verbose:
            print("Validating Positive CloudFormation files...")
        for file in self.cf_files:
            status_parser = self.validate_file(CF_FILES_DIR + file)

            # Status in CF set should be True
            self.cf_states[file] = status_parser
            if status_parser:
                cf_pass += 1
            if verbose:
                print(f'{file[:12]}... | {"PASS - Parsed Successfully" if self.cf_states[file] else "FAIL - Parser Failed"}', end='')
                print()

        if verbose:
            print("\nValidating Negative CloudFormation files...")
        
        for file in self.non_cf_files:
            status_parser = self.validate_file(NON_CF_FILES_DIR + file)

            # Status in non CF set should be False
            self.non_cf_states[file] = status_parser
            if status_parser:
                non_cf_pass += 1
            if verbose:
                print(f'{file[:12]}... | {"PASS - Unable to Parse" if not self.non_cf_states[file] else "FAIL - Parsed Successfully"}')
        
        return self.cf_states, self.non_cf_states, cf_pass, non_cf_pass

    def recompile_grammar(self):
        """
        Recompiles the JSON5.g4 grammar file.

        Returns:
            None
        """
        subprocess.run(GRAMMAR_BUILD_PATH, shell=True)
        return
    
    def get_leaf_nodes(self, currNode = None, leaves = []):
        #TODO: For now, function is outputting all leaf nodes. Need to filter and place
        #      valid pairs (e.g {"Description" : "string"})
        # Could also hard code all leaf values for testing
        """
        Returns the leaf nodes of a given parse tree.

        Args:
            tree (ParseTree): The parse tree to extract leaf nodes from.

        Returns:
            list: A list of leaf nodes.
        """

        if self.curr_tree is None:
            raise Exception("No parse tree found. Please parse a file first.")
        
        currNode = self.curr_tree if currNode is None else currNode
        # print(currNode.getText())
        if currNode.getChildCount() == 0:
            text = currNode.getText()
            if text not in INVALID_ROOTS:
                leaves.append(currNode.getText())
            return leaves
        
        for i in range(currNode.getChildCount()):
            self.get_leaf_nodes(currNode.getChild(i), leaves)

        return leaves

    def get_leaf_nodes_mock(self):
        return {"Description" : "Best Practice SNS Topic", "Type":"String",
                "SNSTopic" : "arn:aws:sns:us-east-1:123456789012:MyTopic", "Domain" : "vpc",
                "Ref" : "Subnet2" }