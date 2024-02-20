ORG_PATH = "JSON5Original.g4"
GRAMMAR_BUILD_PATH = "./build.sh"

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

INITIAL_PAIR_DEF = """pair
    : key ':' value
    ;"""

from CFDataValid import CFDataValid
import subprocess
import os
import random

class g4Refine():
    def __init__(self, g4_target_path):
        # Set our targeted grammar to the original grammar
        with open(ORG_PATH, 'r') as original_file:
            content = original_file.read()
        
        with open(g4_target_path, 'w') as target_file:
            target_file.write(content)

        self.g4_target = g4_target_path
        self.curr_cf_pass = 10
        self.curr_non_cf_pass = 10
        self.curr_g4 = content
        self.curr_pair = INITIAL_PAIR_DEF

        print(self.curr_pair)
    def refine(self, output_path: str = None, verbose: bool = False):
        g_prime, change = self.specialize(self.g4_target)
        
        if output_path is None:
            output_path = self.g4_target

        if not os.path.exists(output_path):
            open(output_path, 'a').close()

        with open(output_path, 'w') as output_file:
            output_file.write(g_prime)

        # Compile grammar's lexer and parser
        subprocess.run(GRAMMAR_BUILD_PATH, shell=True)

        # Validate parser with our dataset
        currValidator = CFDataValid()
        cf_states, non_cf_states, cf_pass, non_cf_pass = currValidator.validate_parser(verbose=verbose)

        # If fewer non-cf files are passing and all cf files are still passing, then we have a better grammar
        # If not, then we need to revert the change to the grammar
        
        # if cf_pass < self.curr_cf_pass:


            
            

        if verbose:
            print(f"CF Pass Change: {self.curr_cf_pass} -> {cf_pass} | Non-CF Pass Change: {self.curr_non_cf_pass} -> {non_cf_pass}")


    def specialize(self, target_path, file_sample_change, change_list = None, verbose = False):
        """
        Runs an iterative change on the target grammar file

        Args:
            target_path (str): The path to the target grammar file
            file_sample_change (str): The file path where we want to sample change
            change_list (list): A list of changes already attempted 
        """

        #TODO: Finalize purpose and functionality of this function

        validator = CFDataValid()
        validator.validate_file(file_sample_change, verbose=verbose)
        leafs = validator.get_leaf_nodes()
        prev_pair = self.curr_pair
    
        if change_list is None:
            change_list = list()
        
        # Choose a random item from leafs that is not in the change_list
        random_leaf_change = random.choice([leaf for leaf in leafs if leaf not in change_list])

        # Apply the change to the grammar
        # if self.curr_pair == INITIAL_PAIR_DEF:
            
        

        # Update the current grammar and pair
        self.curr_g4 = g_prime
        self.curr_pair = random_leaf

        # Add the change to the change_list
        change_list.append(random_leaf)

        # Return the updated grammar and change_list
        return g_prime, change_list
        
        
