import os

from dotenv import load_dotenv

from fastapi import FastAPI
from pydantic import BaseModel, Field

load_dotenv()

app = FastAPI(title="Deploy con Azure", version="1.0.0")


class PostInput(BaseModel):
    nombre: str = Field(min_length=1)
    edad: float = Field(ge=0)
    numeroN: float = Field(gt=0)


class PostOutput(BaseModel):
    frase: str
    calculo: float


@app.get("/")
def get_name() -> dict[str, str]:
    nombre = os.getenv("FIRST_NAME", "TuNombre")
    apellido = os.getenv("LAST_NAME", "TuApellido")
    return {"nombre": nombre, "apellido": apellido}


@app.get("/{number}")
def calculate(number: int) -> dict[str, int]:
    return {"resultado": (number + 5) * 2}


@app.post("/", response_model=PostOutput)
def build_phrase(payload: PostInput) -> PostOutput:
    division = payload.edad / payload.numeroN
    frase = f"{payload.nombre}, tu edad dividida por {payload.numeroN} es {division}"
    return PostOutput(frase=frase, calculo=division)
