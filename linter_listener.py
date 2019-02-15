import sys
sys.path.insert(0, './helpers')

import re
import numpy as np
from Python3Lexer import Python3Lexer
from Python3Parser import Python3Parser
from Python3Listener import Python3Listener
from linter_error_message import LinterErrorMessage
from token_handler import TokenHandler


class LinterListener(Python3Listener):

    def __init__(self, token_stream):
        self.variable = True
        self.token_stream = token_stream
        
        self.token_handler = TokenHandler()
        self.linter_error_message = LinterErrorMessage()        
        
        print("initializing context test with listener...")
    
    def enterAtom(self, ctx:Python3Parser.FuncdefContext):
        pass

    def exitAtom(self, ctx:Python3Parser.FuncdefContext):
        
        actual_token = self.token_handler.get_actual_token(self.token_stream, ctx)
           
        var_name = str(ctx.NAME())

        if var_name != "None":
            
            # Lower case validation for variables PEP8
            lower_case_regex = re.compile("([a-z][a-z0-9_]+)+")
            
            if "INVALID" in var_name:
                pass
            elif lower_case_regex.match(var_name) is None:
                self.linter_error_message.variable_naming_error(var_name, 
                                                                actual_token)

            # Names to avoid validation for variables PEP8

            if var_name == "l" or var_name == "O" or var_name == "I":
                self.linter_error_message.name_to_avoid_error(var_name,
                                                              actual_token)
    def enterClassdef(self, ctx:Python3Parser.ClassdefContext):
        pass

    def exitClassdef(self, ctx:Python3Parser.ClassdefContext):
        actual_token = self.token_handler.get_actual_token(self.token_stream, ctx)
        
        class_name = str(ctx.NAME())
        camel_case_regex = re.compile("([A-Z][a-z0-9]*)+")
        
        if "INVALID" in class_name:
            pass
        elif camel_case_regex.match(class_name) is None:
            self.linter_error_message.class_naming_error(class_name, 
                                                         actual_token)
            
    def enterFuncdef(self, ctx:Python3Parser.FuncdefContext):
        pass

    def exitFuncdef(self, ctx:Python3Parser.FuncdefContext):
        actual_token = self.token_handler.get_actual_token(self.token_stream, ctx)
           
        func_name = str(ctx.NAME())
        lower_case_regex = re.compile("([a-z][a-z0-9_]+)+")
        
        if "INVALID" in func_name:
            pass
        elif lower_case_regex.match(func_name) is None:
            self.linter_error_message.function_naming_error(func_name, 
                                                            actual_token)