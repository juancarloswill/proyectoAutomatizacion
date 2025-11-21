from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "hola mundo"}

@app.get("/healthz")
async def healthz():
    return {"ok": True}