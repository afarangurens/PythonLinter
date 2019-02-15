import sys
sys.path.insert(0, './helpers')

import re
import numpy as np
from Python3Lexer import Python3Lexer
from Python3Parser import Python3Parser
from Python3Listener import Python3Listener
from linter_error_message import LinterErrorMessage
from token_handler import TokenHandler
from style_convention_check import StyleConventionCheck


class LinterListener(Python3Listener):

    def __init__(self, token_stream):
        self.variable = True
        self.token_stream = token_stream
        
        self.token_handler = TokenHandler
        self.linter_error_message = LinterErrorMessage()
        self.convention_checker = StyleConventionCheck 
        
        print("initializing context test with listener...")

    def exitAtom(self, ctx:Python3Parser.AtomContext):
        
        actual_token = self.token_handler.get_actual_token(self.token_stream, ctx, 0)
    
        var_name = str(ctx.NAME())
        lower_case_regex = "([a-z][a-z0-9_]*)+"

        if var_name != "None":

            # Lower case validation for variables PEP8
            var_naming_error = self.linter_error_message.variable_naming_error(
                                                                    var_name, 
                                                                    actual_token)
            self.convention_checker.check_naming_convention(var_name,
                                                            lower_case_regex,
                                                            var_naming_error)

            # Names to avoid validation for variables PEP8
            if var_name == "l" or var_name == "O" or var_name == "I":
                self.linter_error_message.name_to_avoid_error(var_name,
                                                              actual_token)

    def exitClassdef(self, ctx:Python3Parser.ClassdefContext):
        actual_token = self.token_handler.get_actual_token(self.token_stream, ctx, 1)
        
        class_name = str(ctx.NAME())
        camel_case_regex = "([A-Z][a-z0-9]*)+"
        class_naming_error = self.linter_error_message.class_naming_error(
                                                                class_name, 
                                                                actual_token)
                                                                
        self.convention_checker.check_naming_convention(class_name,
                                                        camel_case_regex,
                                                        class_naming_error)
        
        
            

    def exitFuncdef(self, ctx:Python3Parser.FuncdefContext):
        actual_token = self.token_handler.get_actual_token(self.token_stream, ctx, 1)
        
        func_name = str(ctx.NAME())
        lower_case_regex = re.compile("([a-z][a-z0-9_]*)+")
        func_naming_error = self.linter_error_message.function_naming_error(
                                                                func_name, 
                                                                actual_token)

        self.convention_checker.check_naming_convention(func_name,
                                                        lower_case_regex,
                                                        func_naming_error)

            