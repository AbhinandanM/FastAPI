from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
# Adding a cross origin middleware to make api accesible over requests from different ports/origins
origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Home page of the api


@app.get("/")
async def root():
    return {"message": "Hello World"}

# API call endpoint to calculate and return nth Fibonacci (1< n < 100) with time complexity of worse: O(N) best: O(1)


@app.get("/returnFibonacci/")
def Fibonacci(n: int):
    try:
        if n < 1 or n > 100:
            return {'Error': "The number is out of bounds"}
        else:
            a = 0
            b = 1
            for i in range(2, n+1):
                c = a + b
                a = b
                b = c
            return {f"{n}th Fibonacci number is": b}

    except Exception as e:
        return e

# API call endpoint to calculate and return the factorial of a given number with time complexity of O(n*n)


@app.get("/returnFactorial/")
def Factorial(n: int):
    try:
        if n < 0:
            return {'Error': "The number is invalid"}
        else:
            factorial = 1
            for i in range(1, n+1):
                factorial = factorial*i
            return {f"The factorial of {n} is": factorial}

    except Exception as e:
        return e


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
