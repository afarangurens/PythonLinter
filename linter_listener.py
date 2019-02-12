import re
import numpy as np
from Python3Lexer import Python3Lexer
from Python3Parser import Python3Parser
from Python3Listener import Python3Listener
from linter_error_message import LinterErrorMessage


class LinterListener(Python3Listener):

    def __init__(self, token_stream):
        self.variable = True
        self.token_stream = token_stream
        self.linter_error_message = LinterErrorMessage()
        print("initializing context test with listener...")
    
    def enterClassdef(self, ctx:Python3Parser.ClassdefContext):
        pass

    def exitClassdef(self, ctx:Python3Parser.ClassdefContext):
        initial_token = str(ctx.start)
        initial_token_index = int(initial_token[2])
        
        actual_token_index = initial_token_index + 1
        actual_token = str(self.token_stream.get(actual_token_index))
        
        class_name = str(ctx.NAME())
        camel_case_regex = re.compile("([A-Z][a-z0-9]+)+")
        
        if "INVALID" in class_name:
            pass
        elif camel_case_regex.match(class_name) is None:
            self.linter_error_message.class_naming_error(class_name, 
                                                         actual_token)
            
    
