from cachetools import TTLCache
from sqlmodel import Session
from app.crud import get_db_transformed_string,save_db_transformed_string
TRANSFORMED_STRINGS=TTLCache(maxsize=1000, ttl=7200)


def get_db_ts(text:str, session: Session):
    db_transformed_string=get_db_transformed_string(text,session)
    if db_transformed_string is None:
        db_transformed_string=save_db_transformed_string(text,session)
    return db_transformed_string



def get_cached_transformed_string(text:str, session: Session)-> str:
    
    if TRANSFORMED_STRINGS.get(text) is None:
        # Search db if not found in cache
        db_ts=get_db_ts(text,session)
        TRANSFORMED_STRINGS[text]=db_ts.transformed
    return TRANSFORMED_STRINGS[text]


