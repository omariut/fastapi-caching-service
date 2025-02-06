from fastapi import FastAPI,Depends,HTTPException,status
from sqlmodel import Session

from app.schemas import PayloadCreate, PayloadRead
from app.utils import generate_output
from app.database import init_db,engine
from app.crud import save_db_payload,get_db_payload_by_id
app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_db()

def get_session():
    with Session(engine) as session:
        yield session

@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok", "message": "Service is running"}


@app.post("/payload",status_code=status.HTTP_201_CREATED)
async def create_payload(payload: PayloadCreate,session: Session = Depends(get_session)):
    list1 = payload.list_1
    list2 = payload.list_2
    output = generate_output(list1, list2,session)
    db_payload=save_db_payload(output,session)
    return {
        "id": db_payload.id,
        "message": "Successs",
        
            }

@app.get("/payload/{payload_id}", response_model=PayloadRead)
def read_payload(payload_id: int, session: Session = Depends(get_session)):
    payload = get_db_payload_by_id(payload_id,session)
    if not payload:
        raise HTTPException(status_code=404, detail="Payload not found")
    return payload


