
"""
This file runs a demo for the refine function in g4Refine.py
This will demonstrate a basic refinement to the grammar
NOTE: Demo is currently implemented in the g4Refine.py file.
      Refer to the file for the demo implementation
"""

from antlr4 import *
from g4Refine import g4Refine
from grammarinator import *

def main():
    refiner = g4Refine()
    refiner.refine_demo()

if __name__ == '__main__':
    main()