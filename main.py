from fastapi import FastAPI
from pydantic import BaseModel
from starlette.requests import Request
from starlette.responses import Response, JSONResponse

app = FastAPI()

@app.get('/ping')
def read_ping ():
    return Response

@app.post('/cars')

@app.get("/cars")

@app.get('/cars/{id}')

@app.put('/cars/{id}/characteristics')