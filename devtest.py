from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def is_armstrong(number: int) -> bool:
    digits = [int(d) for d in str(number)]
    armstrong_sum = sum(d ** len(digits) for d in digits)
    return armstrong_sum == number

@app.get("/api/classify-number")
async def classify_number(number: str):
    if not number.isdigit():
        raise HTTPException(status_code=400, detail="Input should be a valid integer")

    number = int(number)
    is_prime = number > 1 and all(number % i != 0 for i in range(2, int(number ** 0.5) + 1))
    is_perfect = number == sum(i for i in range(1, number) if number % i == 0)
    armstrong = is_armstrong(number)
    properties = []
    if armstrong:
        properties.append("armstrong")
    properties.append("even" if number % 2 == 0 else "odd")
    
    digit_sum = sum(int(d) for d in str(number))
    async with httpx.AsyncClient() as client:
        response = await client.get(f"http://numbersapi.com/{number}/math")
        fun_fact = response.text.strip()

    result = {
        "number": number,
        "is_prime": is_prime,
        "is_perfect": is_perfect,
        "properties": properties,
        "digit_sum": digit_sum,
        "fun_fact": fun_fact
    }

    return JSONResponse(content=result)

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "number": request.query_params.get("number", "alphabet"),
            "error": True,
        },
    )
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)