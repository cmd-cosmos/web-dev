#type: ignore
#pylint: skip-file

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class RocketObject(BaseModel):
    id : int
    name : str
    score : float

@app.get("/")
def root():
    return {
        "Data" : "Test Data"
    }