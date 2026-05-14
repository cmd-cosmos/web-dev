#type: ignore
#pylint: skip-file

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
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

@app.get("/rockets", response_class=HTMLResponse)
def rockets():
    return """
    <html>
        <head>
            <title>Rockets</title>
        </head>
        <body>
            <h>Rockets</h>
            <p>Rockets are really cool, they go to space.</p>
        </body>
        
    </html>
"""