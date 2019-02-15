class TokenHandler:
    def get_actual_token(self, token_stream, context):
        initial_token = str(context.start)
        initial_token_index = int(initial_token[2])
        
        actual_token_index = initial_token_index + 1
        actual_token = str(token_stream.get(actual_token_index))

        return actual_token
