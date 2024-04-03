
"""
This file runs a demo for the specialize function in g4Refine.py
This will demonstrate how the grammar is being refined fundamentally
NOTE: Demo is currently implemented in the g4Refine.py file.
      Refer to the file for the demo implementation
"""

import sys
from antlr4 import *
from g4Refine import g4Refine
from grammarinator import *

def main():
    refiner = g4Refine()
    refiner.specialize_demo()

if __name__ == '__main__':
    main()