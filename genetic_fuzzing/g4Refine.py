ORG_PATH = "JSON5Original.g4"
EDIT_PATH = "JSON5.g4"
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
CF_FILES_DIR = "cf_json/"

INITIAL_PAIR_DEF = """pair
    : key ':' value
    ;"""

UPDATE_PAIR_STR = """pair
    :"""

LEXER_STR = """// Lexer"""

from CFDataValid import CFDataValid
import pickle
import json
import os
import random
from CFDataValid import CFDataValid
import subprocess
import os
import random

class g4Refine():
    def __init__(self):
        # Set our targeted grammar to the original grammar
        with open(ORG_PATH, 'r') as original_file:
            content = original_file.read()
        with open(EDIT_PATH, 'w') as target_file:
            target_file.write(content)

        self.curr_g4 = content
        self.prev_pair = INITIAL_PAIR_DEF

        # TODO: Mark change
        self.change_list = {}

        # TODO: Add system check. Validate cf files, non-cf files, compile grammar, etc.
    
    # NOTE: This just applies one change. Will be using "SNSTopic.json", but does
    #       do anything at this time
    # TODO: Apply multiple changes
        
    def refine(self, verbose: bool = False):
        if verbose: print(f"Refining Grammar")
        g_prime, new_pair = self.specialize(CF_FILES_DIR + "SNSTopic.json", verbose=True)
        if verbose: print(f"DONE!\n")

        # Write the new grammar to the file
        if not os.path.exists(EDIT_PATH):
            open(EDIT_PATH, 'a').close()

        if verbose: print(f"Writing modifed grammar to: {EDIT_PATH}")
        with open(EDIT_PATH, 'w') as output_file:
            output_file.write(g_prime)
        if verbose: print(f"DONE!\n")

        # Compile grammar's lexer and parser
        currValidator = CFDataValid()
        if verbose: print(f"Compiling New Lexer & Parser Files...")
        currValidator.recompile_grammar()
        if verbose: print(f"DONE!\n")

        # Validate parser with our dataset
        cf_states, non_cf_states, cf_pass, non_cf_pass = currValidator.validate_parser(verbose=verbose)

        # TODO: Set condition for accepting grammar change. For now, we will just make a change regardless of status
        # If fewer non-cf files are passing and all cf files are still passing, then we have a better grammar
        # If not, then we need to revert the change to the grammar
        
        # Grammar Valid
        self.curr_g4 = g_prime
        self.prev_pair = new_pair

        print(f"New Grammar Saved")

        # if verbose:
        #     print(f"CF Pass Change: {self.curr_cf_pass} -> {cf_pass} | Non-CF Pass Change: {self.curr_non_cf_pass} -> {non_cf_pass}")

    def refine_demo(self):
        import tkinter as tk
        from tkinter import messagebox

        print("RYFOK GRAMMAR REFINEMENT DEMO V0.1\n")
        print("-----------------------------------")
        input("Refining Grammar: Press any key to continue...")
        print(f"Refining...")
        g_prime, new_pair = self.specialize(CF_FILES_DIR + "SNSTopic.json", verbose=True)
        print(f"---------------DONE----------------")

        input("Write new grammar to file: Press any key to continue...")
        print(f"Writing...")
        # Write the new grammar to the file
        if not os.path.exists(EDIT_PATH):
            open(EDIT_PATH, 'a').close()
        with open(EDIT_PATH, 'w') as output_file:
            output_file.write(g_prime)
        print(f"---------------DONE----------------")
        # Read the file content
        with open(EDIT_PATH, 'r') as file:
            content = file.read()

        # Create a Tkinter window
        window = tk.Tk()
        window.withdraw()  # Hide the main window

        # Display the file content in a popup window
        messagebox.showinfo("Grammar", content[:800])

        # Close the Tkinter window
        window.destroy()

        input("Update ANTLR4 Generated Files: Press any key to continue...")
        # Compile grammar's lexer and parser
        currValidator = CFDataValid()
        print(f"Compiling...")
        currValidator.recompile_grammar()
        print(f"---------------DONE----------------")
        
        input("Evaluate New Grammar Performance: Press any key to continue...")
        print(f"Evaluating...")
        # Validate parser with our dataset
        cf_states, non_cf_states, cf_pass, non_cf_pass = currValidator.validate_parser(verbose=True)
        print(f"---------------DONE----------------")

        reset = input("Demo is finished. Reset to original grammar? (y/n): ")
        if reset.lower() == "y":
            print(f"Resetting...")
            with open(ORG_PATH, 'r') as original_file:
                content = original_file.read()
            with open(EDIT_PATH, 'w') as target_file:
                target_file.write(content)
            print(f"Original Grammar Restored. Recompiling...")
            currValidator.recompile_grammar()
            print(f"---------------DONE----------------")
            print(f"Original Grammar Restored")

    def specialize_demo(self):
        print("RYFOK GRAMMAR SPECIALIZATION DEMO V0.1\n")
        print("-----------------------------------")
        sampleFile = CF_FILES_DIR + "SNSTopic.json"

        validator = CFDataValid()
        validator.validate_file(sampleFile)
        leafs = validator.get_leaf_nodes_mock()
        print(f"Leaf Nodes: {leafs}")
        
        prev_pair = self.prev_pair
    
        if sampleFile not in self.change_list:
            self.change_list[sampleFile] = list()

        change_list = self.change_list[sampleFile]
        
        for i in range(len(leafs)):
            input(f"Specialize with a random leaf {i}: Press ENTER key to continue...")
            random_leaf_change = random.choice([key for key in leafs.keys() if key not in change_list])
            change_list.append(random_leaf_change)
            print(f"\nSelected Leaf: \'{random_leaf_change}\' : \'{leafs[random_leaf_change]}\'\n")      
            new_pair, new_rule = self.add_to_pair(random_leaf_change, leafs[random_leaf_change])

            print(f"New Rule\n--------\n\n {new_rule}\n")
            print(f"Updated Pair\n--------\n\n {new_pair}\n")

            # Apply the change to the grammar
            new_g4 = self.curr_g4.replace(prev_pair, new_pair)
            new_g4 += "\n" + new_rule
            self.prev_pair = new_pair
        print("ALL LEAFS ADDED. TERMINATING...")
        
    def specialize(self, sampleFile, verbose = False):
        """
        Runs an iterative change on the target grammar file

        Args:
            sampleFile (str): The file to extract a mutation from
            verbose (bool): If True, prints the new rule and pair
        Return:
            new_g4 (str): The updated grammar file
            new_pair (str): The updated pair definition
        """

        validator = CFDataValid()
        validator.validate_file(sampleFile, verbose=verbose)

        # Create a new directory called parse_tree
        if not os.path.exists("parse_tree"):
            os.makedirs("parse_tree")

        # Run the command to generate the parse tree
        os.system(f"grammarinator-parse {EDIT_PATH} -r json5 -i {sampleFile} -o parse_tree")

        # Obtain the single .grt file in the parse_tree folder
        grt_files = [file for file in os.listdir("parse_tree") if file.endswith(".grt")]
        if len(grt_files) != 1:
            raise Exception ("Error: Expected a single .grt file in the parse_tree folder.")
        grt_file = grt_files[0]
        grt_file_path = os.path.join("parse_tree", grt_file)
        # Open the .grt file
        with open(grt_file_path, 'rb') as file:
            content = open(grt_file_path, 'rb')
        pickle_file = pickle.load(content)
        content_dict = json.loads(pickle_file.__str__())
        tree = validator.traverse_antlr_pre_order(content_dict, verbose=verbose)
        
        #TODO: Cannot delete because resource is being used. FIX ASAP
        prev_pair = self.prev_pair
    
        if sampleFile not in self.change_list:
            self.change_list[sampleFile] = list()
        else:
            raise ValueError("Sample file already in change list. Specialization can only be performed once per file.")

        change_list = self.change_list[sampleFile]
        
        # Choose a random item from leafs that is not in the change_list
        # TODO: Increase coverage for nested lists
        random_leaf_change = random.choice([key for key in tree.keys() if key not in change_list])
        change_list.append(random_leaf_change)
        if verbose: print(f"Selected Leaf: \'{random_leaf_change}\' : \'{tree[random_leaf_change]}\'\n")      
        new_pair, key_parser_rule, value_parser_rule, new_lexer_key, new_lexer_value = self.submit_change(random_leaf_change, tree[random_leaf_change])

        if verbose:           
            full_pair = new_pair + "\n\n" + key_parser_rule + "\n\n" + value_parser_rule
            full_new_lexer = LEXER_STR +"\n\n" + new_lexer_key + "\n\n" + new_lexer_value
            print(f"Full Pair + Rules\n{full_pair}")
            print("------------------")
            print(f"New Lexer Rules\n{full_new_lexer}")

        # Apply the change to the grammar
        new_g4 = self.curr_g4.replace(INITIAL_PAIR_DEF, full_pair)
        new_g4 = new_g4.replace(LEXER_STR, full_new_lexer)

        return new_g4, new_pair
            
        # # Update the current grammar and pair
        # self.curr_g4 = g_prime
        # self.prev_pair = random_leaf

        # # Add the change to the change_list
        # change_list.append(random_leaf)

        # # Return the updated grammar and change_list
        # return g_prime, change_list

    # NOTE: This function only takes in string key and values, 
    #       but we still need to consider object key/values
    def submit_change(self, key: str, value):
        """
        Obtains new rules based off key-value pair to add to the grammar

        Args:
            key (str): The key to add to the pair definition
            value (str): The value to add to the pair definition
        Return:
            new_pair (str): The updated pair definition
            key_parser_rule (str): key parser rule
            value_parser_rule (str): value parser rule
            new_lexer_key (str): lexer rule for the key
            new_lexer_value (str): lexer rule for the value
        """

        new_rule = INITIAL_PAIR_DEF
        rule_key_name = key.replace(" ", "").lower() + "Keys"
        rule_value_name = key.replace(" ", "").lower() + "Values"
        lexer_key_name = key.replace(" ", "").upper() + "_KEY"
        lexer_value_name = key.replace(" ", "").upper() + "_VALUE"

        ### Generate new rule

        # new pair set
        new_rule_value = f"""{rule_key_name} ':' {rule_value_name}"""

        # new lexer rules
        new_lexer_key = new_rule.replace("""pair""", lexer_key_name)
        new_lexer_key = new_lexer_key.replace(""": key ':' value""", f""": \'\"{key}\"\'""")

        new_lexer_value = new_rule.replace("""pair""", lexer_value_name)
        new_lexer_value_syntax = ""
        if type(value) == str:
            new_lexer_value_syntax = f""": \'\"\' \'{value}\' \'\"\'"""
        elif type(value) == list:
            for i, val in enumerate(value):
                if i == 0:
                    new_lexer_value_syntax += f""": \'\"\' {val[0]} \'\"\'"""
                else:
                    new_lexer_value_syntax += f"""
    | \'\"\' {val[0]} \'\"\'"""
        else:
            # TODO: Need to expand coverage
            raise ValueError("Value must be a string or list of strings. Different types are WIP")
        new_lexer_value = new_lexer_value.replace(""": key ':' value""", new_lexer_value_syntax)

        # new parser rules
        key_parser_rule = new_rule.replace("""pair""", rule_key_name)
        key_parser_rule = key_parser_rule.replace(""": key ':' value""", f""": {lexer_key_name}""")
        value_parser_rule = new_rule.replace("""pair""", rule_value_name)
        value_parser_rule = value_parser_rule.replace(""": key ':' value""", f""": {lexer_value_name}""")   

        # TODO: Need to expand coverage
        replace_pair_str = f"""pair
    : {new_rule_value}
    |"""

        # Add rule subset into pair definition
        new_pair = self.prev_pair
        new_pair = new_pair.replace(UPDATE_PAIR_STR, replace_pair_str)
        # print(new_pair)
        return new_pair, key_parser_rule, value_parser_rule, new_lexer_key, new_lexer_value
    
    def refine_demo_2(self):
        import tkinter as tk
        from tkinter import messagebox

        print("RYFOK GRAMMAR REFINEMENT DEMO V1.0\n")
        print("-----------------------------------")
        input("Refining Grammar: Press ENTER to continue...")
        print(f"Refining...")
        g_prime, new_pair = self.specialize("testJSON.json5", verbose=True)
        print(f"---------------DONE----------------")

        input("Write new grammar to file: Press ENTER to continue...")
        print(f"Writing...")
        # Write the new grammar to the file
        if not os.path.exists(EDIT_PATH):
            open(EDIT_PATH, 'a').close()
        with open(EDIT_PATH, 'w') as output_file:
            output_file.write(g_prime)
        print(f"---------------DONE----------------")
        # Read the file content
        with open(EDIT_PATH, 'r') as file:
            content = file.read()

        input("Update ANTLR4 Generated Files: Press ENTER to continue...")
        # Compile grammar's lexer and parser
        currValidator = CFDataValid()
        print(f"Compiling...")
        currValidator.recompile_grammar()
        print(f"---------------DONE----------------")
        
        input("Evaluate New Grammar Performance: Press ENTER to continue...")
        print(f"Evaluating...")
        # Validate parser with our dataset
        cf_states, non_cf_states, cf_pass, non_cf_pass = currValidator.validate_parser(verbose=True)
        print(f"---------------DONE----------------")

        reset = input("Demo is finished. Reset to original grammar? (y/n): ")
        if reset.lower() == "y":
            print(f"Resetting...")
            with open(ORG_PATH, 'r') as original_file:
                content = original_file.read()
            with open(EDIT_PATH, 'w') as target_file:
                target_file.write(content)
            print(f"Original Grammar Restored. Recompiling...")
            currValidator.recompile_grammar()
            print(f"---------------DONE----------------")
            print(f"Original Grammar Restored")
        # Delete all files in parse_tree folder
        file_list = os.listdir("parse_tree")
        for file_name in file_list:
            file_path = os.path.join("parse_tree", file_name)
            if os.path.isfile(file_path):
                os.remove(file_path)

    def add_to_pair(self, key: str, value: str):
        """
        Adds a pair to the current pair definition

        Args:
            key (str): The key to add to the pair definition
            value (str): The value to add to the pair definition
        Return:
            new_pair (str): The updated pair definition
            new_rule (str): The new rule to add to the grammar
        """

        new_rule = INITIAL_PAIR_DEF

        # Generate new rule
        new_rule_value = f""": \'{key}\' ':' \'{value}\'"""
        new_rule_name = key.replace(" ", "").lower() + "Pair"
        new_rule = new_rule.replace("""pair""", new_rule_name)
        new_rule = new_rule.replace(""": key ':' value""", new_rule_value)

        # print(new_rule)

        # TODO: Takes in only string key and values.
        replace_pair_str = f"""pair
    : {new_rule_name}
    |"""

        # Add rule into grammar
        new_pair = self.prev_pair
        new_pair = new_pair.replace(UPDATE_PAIR_STR, replace_pair_str)

        return new_pair, new_rule
