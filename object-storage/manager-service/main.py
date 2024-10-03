from typing import Union
from fastapi import FastAPI

app = FastAPI()

def queryObject():
    return 

@app.get("/query-object/uuid/{uuid}")
def read_item(uuid: str):
    return {"uuid": uuid}

@app.get("/query-object/filename/{filename}")
def read_item(filename: str):
    return {"uuid": uuid}