import re
import sys
sys.path.insert(0, './helpers')


class LinterErrorMessage:
    
    def show_error_position(self, token_str):
        line_col_regex = ('((?<=,)([0-9]+[:][0-9]+)(?=]))')
        line_col = re.findall(line_col_regex, token_str)[0][0]

        error_position_message = "in line {}".format(line_col)
        return error_position_message

    def class_naming_error(self, class_name, token_str):
        error_position = self.show_error_position(token_str)
        
        class_naming_error = ("Style Error {}, the class '{}' is not using"
                              " CamelCase convention".format(error_position, 
                                                             class_name))
        return class_naming_error                                                             

    def max_line_chars_error(self, token_str, token_text):
        error_position = self.show_error_position(token_str)

        max_char_error = ("Style Error: {} {} exceedes the 79 maximum line"
                          " characters ".format(token_text, error_position))
        return max_char_error                          

    def indentation_error(self, token_str):
        error_position = self.show_error_position(token_str)

        indent_error = ("Style Error {}, wrong indentation"
                       " level ".format(error_position))
        return indent_error

    def variable_naming_error(self, var_name, token_str):
        error_position = self.show_error_position(token_str)

        var_naming_error = ("Style Error {}, the variable '{}' is not using"
                           " lowercase-separated by underscore"
                           " format".format(error_position, var_name))
        return var_naming_error                           
    
    def function_naming_error(self, func_name, token_str):
        error_position = self.show_error_position(token_str)

        func_naming_error = ("Style Error {}, the function '{}' is not using"
                            " lowercase-separated by underscore"
                            " format".format(error_position, func_name))
        return func_naming_error                            
    
    def function_arglist_error(self, token_str):
        error_position = self.show_error_position(token_str)

        arglist_error = ("Style Error {} function has too many arguments"
                         "(Max arguments sugested: 3)".format(error_position))
        return arglist_error

    def name_to_avoid_error(self, var_name, token_str):
        error_position = self.show_error_position(token_str)

        avoid_name_error = ("Style Error {}, the variable '{}' is in the"
                            " list of 'names to avoid' in python"
                            " ('l', 'O', I)".format(error_position, var_name))
        return avoid_name_error     

    def operator_space_error(self, token_str, symbol):
        error_position = self.show_error_position(token_str)
        
        comma_space_error = ("Style Error {}, missing a blank space"
                            " after '{}'".format(error_position, symbol))
        return comma_space_error

    def const_naming_error():
        error_position = self.show_error_position(token_str)

        const_naming_error = ("Style Error {}, the constant '{}' is"
                             " not using UPERCASE-separated by underscore"
                             " format".format(error_position, var_name))
        return const_naming_error