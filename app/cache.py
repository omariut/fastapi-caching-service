from cachetools import TTLCache
from app.transformer import transformer_function
TRANSFORMED_STRINGS=TTLCache(maxsize=1000, ttl=7200)

def get_cached_transformed_string(text:str)-> str:
    
    if TRANSFORMED_STRINGS.get(text) is None:
        transformed_text=transformer_function(text)
        TRANSFORMED_STRINGS[text]=transformed_text
    return TRANSFORMED_STRINGS[text]


