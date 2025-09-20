from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from mangum import Mangum

app = FastAPI(title="Calculator API")

class Operands(BaseModel):
    a: float
    b: float

@app.post("/add")
def add(operands: Operands):
    return {"result": operands.a + operands.b}

@app.post("/subtract")
def subtract(operands: Operands):
    return {"result": operands.a - operands.b}

@app.post("/multiply")
def multiply(operands: Operands):
    return {"result": operands.a * operands.b}

@app.post("/divide")
def divide(operands: Operands):
    if operands.b == 0:
        raise HTTPException(status_code=400, detail="Division by zero is not allowed")
    return {"result": operands.a / operands.b}

# AWS Lambda handler
handler = Mangum(app)
