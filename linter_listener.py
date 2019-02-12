import re
from Python3Lexer import Python3Lexer
from Python3Parser import Python3Parser
from Python3Listener import Python3Listener


class LinterListener(Python3Listener):

    def __init__(self):
        self.variable = True
        print("initializing context test with listener...")
    
    def enterClassdef(self, ctx:Python3Parser.ClassdefContext):
        pass

    def exitClassdef(self, ctx:Python3Parser.ClassdefContext):
        class_name = str(ctx.NAME())
        camel_case_regex = re.compile("([A-Z][a-z0-9]+)+")

        if "INVALID" in class_name:
            pass
        elif camel_case_regex.match(class_name) is None:
            print("ERROR")
    
