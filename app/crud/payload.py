from sqlmodel import Session, select
from app.models import Payload

def get_db_payload_by_output(session: Session, output: str) -> Payload:
    return session.exec(select(Payload).where(Payload.output == output)).first()

def get_db_payload_by_id(session: Session, id: int) -> Payload:
    return session.exec(select(Payload).where(Payload.id == id)).first()

def save_db_payload(output:str,session: Session)-> Payload:
    db_payload=get_db_payload_by_output(output=output,session=session)
    if db_payload:
        return db_payload
    new_payload = Payload(output=output)
    session.add(new_payload)
    session.commit()
    session.refresh(new_payload)
    return new_payload

