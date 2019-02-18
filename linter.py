import sys
from antlr4 import *
from Python3Lexer import Python3Lexer
from Python3Parser import Python3Parser
from linter_listener import LinterListener

def main():
    input_file = sys.argv[1]
    input = FileStream(input_file)
    lexer = Python3Lexer(input)
    stream = CommonTokenStream(lexer)
    parser = Python3Parser(stream)
    tree = parser.file_input()
    
    linter_listener = LinterListener(stream)
    walker = ParseTreeWalker()
    walker.walk(linter_listener, tree)


if __name__ == '__main__':
    main()