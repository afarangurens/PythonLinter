class LinterErrorMessage:

    def show_error_position(self, token):
        error_position = token[-4:-1]
        error_position_message = "in line {}".format(error_position)
        return error_position_message

    def class_naming_error(self, class_name, token):
        error_position = self.show_error_position(token)
        
        class_naming_error = ("Style Error {}, the class '{}' is not using"
                              " CamelCase convention".format(error_position, 
                                                             class_name))
        return class_naming_error                                                             

    def max_line_chars_error(self, token):
        error_position = self.show_error_position(token)

        max_char_error = ("Style Error {}, the line has more"
                          " than 79 characters ".format(error_position))
        return max_char_error                          

    def indentation_error(self, token):
        error_position = self.show_error_position(token)

        indent_error = ("Style Error {}, wrong indentation"
                       " level ".format(error_position))
        return indent_error

    def variable_naming_error(self, var_name, token):
        error_position = self.show_error_position(token)

        var_naming_error = ("Style Error {}, the variable '{}' is not using"
                           " lowercase-separated by underscore"
                           " format".format(error_position, var_name))
        return var_naming_error                           
    
    def function_naming_error(self, func_name, token):
        error_position = self.show_error_position(token)

        func_naming_error = ("Style Error {}, the function '{}' is not using"
                            " lowercase-separated by underscore"
                            " format".format(error_position, func_name))
        return func_naming_error                            
    
    def name_to_avoid_error(self, var_name, token):
        error_position = self.show_error_position(token)

        avoid_name_error = ("Style Error {}, the variable '{}' is in the"
                            " list of 'names to avoid' in python"
                            " ('l', 'O', I)".format(error_position, var_name))
        return avoid_name_error     

    def const_naming_error():
        error_position = self.show_error_position(token)

        const_naming_error = ("Style Error {}, the constant '{}' is"
                             " not using UPERCASE-separated by underscore"
                             " format".format(error_position, var_name))
        return const_naming_error