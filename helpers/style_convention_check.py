import re

class StyleConventionCheck:
    
    def check_naming_convention(actual_name, regex_expression, error_message):
        compiled_regex = re.compile(regex_expression)
        
        if "INVALID" in actual_name:
            pass
        elif compiled_regex.match(actual_name) is None:
            print(error_message)
        