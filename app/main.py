from fastapi import FastAPI, HTTPException, Depends
app = FastAPI()
@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok", "message": "Service is running"}
