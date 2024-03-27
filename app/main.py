from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def sample_message():
    return {"message": "Hello, FastApi!"}