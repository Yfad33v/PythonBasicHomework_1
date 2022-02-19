
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"massage": "Hello World"}

@app.get("/ping")
def ping():
    return {"message": "pong"}

