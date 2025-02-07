from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import math
import requests
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

class NumberResponse(BaseModel):
    number: int
    is_prime: bool
    is_perfect: bool
    properties: list
    digit_sum: int
    fun_fact: str

def is_armstrong(number):
    n = len(str(number))
    return number == sum(int(digit) ** n for digit in str(number))

def digit_sum(number):
    return sum(int(digit) for digit in str(number))

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    return sum(i for i in range(1, n) if n % i == 0) == n

@app.get("/api/classify-number", response_model=NumberResponse)
def classify_number(number: int):
    properties = []
    if is_armstrong(number):
        properties.append("armstrong")

    if number % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")

    response = requests.get(f"http://numbersapi.com/{number}/math")
    fun_fact = response.text if response.status_code == 200 else "No fun fact found."

    result = NumberResponse(
        number=number,
        is_prime=is_prime(number),
        is_perfect=is_perfect(number),
        properties=properties,
        digit_sum=digit_sum(number),
        fun_fact=fun_fact
    )

    return result

@app.exception_handler(ValueError)
def value_error_handler(request, exc):
    return JSONResponse(
        status_code=400,
        content={"error": True, "message": "Alphabet."}
    )
