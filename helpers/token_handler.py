import re

class TokenHandler:
    def get_actual_token(token_stream, context, needs_keyword):
        initial_token = str(context.start)
        initial_token_index = int(re.findall('(?<=@)[0-9]+(?=,)', initial_token)[0])
    
        if needs_keyword:
            actual_token_index = initial_token_index +1
        else:
            actual_token_index = initial_token_index

        actual_token = str(token_stream.get(actual_token_index))
        
        return actual_token
        
