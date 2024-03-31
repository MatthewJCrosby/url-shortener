from fastapi import FastAPI
from app.api.api_handlers import router as api_router

app = FastAPI()

# This file is the entry point for running the FastAPI application and to configure and start the web server.
app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn
    #at a later time, these will become enviroment variables.
    uvicorn.run(app, host="0.0.0.0", port=8000)
