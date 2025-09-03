from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
from starlette.exceptions import HTTPException
from starlette.requests import Request
from starlette.responses import Response, JSONResponse

app = FastAPI()


@app.get("/ping")
def read_ping():
    return JSONResponse(
        content={"pong"},
        status_code=200,
        media_type="text/plain"
    )


class Characteristics(BaseModel):
    max_speed: int
    max_fuel_capacity: int


class Car(BaseModel):
    id: str
    brand: str
    model: str
    characteristics: Characteristics


cars: List[Car] = []


@app.post('/cars', status_code= 201)
def create_cars(car = Car):
    print(f"hi, i work. this: {cars} is the list of cars")
    if any(existing_car.id == car.id for existing_car in cars):
        raise HTTPException(status_code=400, detail="this ID already exists")

@app.get("/cars")
def read_cars():
    return cars