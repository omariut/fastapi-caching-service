from app.transformer import transformer_function


def generate_output(list1: list, list2: list) -> str:
    transformed1 = [transformer_function(text) for text in list1]
    transformed2 = [transformer_function(text) for text in list2]
    
    interleaved = [val for pair in zip(transformed1, transformed2) for val in pair]
    payload = ", ".join(interleaved)
    return payload