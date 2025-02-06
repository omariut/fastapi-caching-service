from sqlmodel import Session, select
from app.transformer import transformer_function
from app.models import TransformedString

def save_db_transformed_string(text:str, session: Session):
    transformed_text=transformer_function(text)
    ts = TransformedString(original=text, transformed=transformed_text)
    session.add(ts)
    session.commit()
    session.refresh(ts)
    return ts     


def get_db_transformed_string(text:str, session: Session)-> TransformedString:
    ts=session.exec(select(TransformedString).where(TransformedString.original == text)).first()
    return ts


