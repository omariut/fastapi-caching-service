from fastapi import FastAPI, HTTPException, Depends
from app.schemas import PayloadCreate, PayloadRead
from app.utils import generate_output

app = FastAPI()
@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok", "message": "Service is running"}


@app.post("/payload", response_model=PayloadRead)
async def create_payload(payload: PayloadCreate):
    list1 = payload.list_1
    list2 = payload.list_2
    output = generate_output(list1, list2)
    return PayloadRead(output=output)