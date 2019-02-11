from antlr4 import *
from Python3Lexer import Python3Lexer
from Python3Parser import Python3Parser
from class_naming_convention_listener import ClassNamingConventionListener

def main():
    input = FileStream("test.py")
    lexer = Python3Lexer(input)
    stream = CommonTokenStream(lexer)
    parser = Python3Parser(stream)
    tree = parser.file_input()

    file_input_listener = ClassNamingConventionListener()
    walker = ParseTreeWalker()
    walker.walk(file_input_listener, tree)


if __name__ == '__main__':
    main()