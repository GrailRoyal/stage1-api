from fastapi import FastAPI, Query, HTTPException
from typing import Union
import requests

app = FastAPI()


# Helper Functions
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n: int) -> bool:
    return sum(i for i in range(1, n) if n % i == 0) == n

def is_armstrong(n: int) -> bool:
    digits = [int(d) for d in str(abs(n))]  # Handle negative numbers correctly
    return sum(d ** len(digits) for d in digits) == abs(n)

def get_fun_fact(n: int) -> str:
    try:
        response = requests.get(f"http://numbersapi.com/{n}/math?json")
        if response.status_code == 200:
            return response.json().get("text", "No fun fact available.")
    except:
        pass
    return "No fun fact available."

# API Endpoint
@app.get("/api/classify-number/")
def classify_number(number: Union[int, float] = Query(..., description="The number to classify")):
    try:
        number = float(number)  # Ensure number is float/int
        if number.is_integer():
            number = int(number)  # Convert to int if it's a whole number
        else:
            raise HTTPException(status_code=400, detail="Only integers are allowed")

    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid input. Please provide a valid number.")

    properties = []
    if is_armstrong(number):
        properties.append("armstrong")
    properties.append("odd" if number % 2 else "even")

    return {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": sum(int(digit) for digit in str(abs(number)) if digit.isdigit()),
        "fun_fact": get_fun_fact(number),
    }

# Run Server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
