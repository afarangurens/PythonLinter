
class LinterErrorMessage:

    def show_error_position(self, token):
        error_position = token[-4:-1]
        error_position_message = "in line {}".format(error_position)
        return error_position_message

    def class_naming_error(self, class_name, token):
        error_position = self.show_error_position(token)
        
        print("Style Error {}, the class name {} is not using"
              " CamelCase convention".format(error_position, class_name))

    def max_line_chars_error(self, token):
        error_position = self.show_error_position(token)

        print("Style Error {}, the line has more than 79 characters ".format(
            error_position))

    def indentation_error(self, token):
        error_position = self.show_error_position(token)

        print("Style Error {}, wrong indentation level ".format(
            error_position))

    def variable_naming_error(self, var_name, token):
        error_position = self.show_error_position(token)

        print("Style Error {}, the variable name {} is not using"
              " lowercase-separated by underscore format".format(error_position,
                                                                var_name))
    
    def function_naming_error(self, func_name, token):
        error_position = self.show_error_position(token)

        print("Style Error {}, the function name {} is not using"
              " lowercase-separated by underscore format".format(error_position,
                                                                func_name))
    
    def name_to_avoid_error(self, var_name, token):
        error_position = self.show_error_position(token)

        print("Style Error {}, the variable name {} is in the list of 'names"
              " to avoid' in python ('l', 'O', I)".format(error_position,
                                                          var_name))
    def const_naming_error():
        error_position = self.show_error_position(token)

        print("Style Error {}, the constant name {} is not using"
              " UPPERCASE-separated by underscore format".format(error_position,
                                                                var_name))
