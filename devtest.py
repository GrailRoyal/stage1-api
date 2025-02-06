from fastapi import FastAPI, Query
import requests

app = FastAPI()

def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_armstrong(n: int) -> bool:
    """Check if a number is an Armstrong number."""
    digits = [int(digit) for digit in str(n)]
    power = len(digits)
    return sum(digit ** power for digit in digits) == n

def is_perfect(n: int) -> bool:
    """Check if a number is a Perfect number."""
    return sum(i for i in range(1, n) if n % i == 0) == n

def get_fun_fact(n: int) -> str:
    """Fetch a fun fact from the Numbers API."""
    response = requests.get(f"http://numbersapi.com/{n}/math")
    return response.text if response.status_code == 200 else "No fun fact available."

def isNumber(number):
    try:
        int(number)
        return True
    except ValueError:
        return False

@app.get("/api/classify-number/")
def classify_number(number = Query(..., description="The number to classify")):
    """API endpoint to classify a number."""

    if not number:
        return {"error": True, "number": "alphabet" }

    if not isNumber(number):
        return {"number": "alphabet" , "error": True}

    properties = []
    
    if is_armstrong(number):
        properties.append("armstrong")
    properties.append("odd" if number % 2 else "even")

    return {
    "number": number,

    "is_prime": is_prime(number),

    "is_perfect": is_perfect(number),

    "properties": properties,

    "digit_sum": sum(int(digit) for digit in str(number)),

    "fun_fact": get_fun_fact(number)
}
if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)