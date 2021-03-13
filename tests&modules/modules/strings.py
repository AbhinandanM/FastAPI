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

# homepage of the api


@app.get("/strings")
async def root():
    return {"message": "Hello World"}

# API call endpoint to generate and return a string of a given length of a chosen character as input


@app.get("/strings/generateString/")
def generateStr(char: str = 'i', count: int = 1):
    try:
        String = char*count
        return {"String": String}
    except Exception as e:
        return e

# API call endpoint to calculate and return the length of a string


@app.get("/strings/getLenOfString/")
def lenOfStr(string: str = 'Welcome'):
    try:
        Length = len(string)
        return {"String length": Length}
    except Exception as e:
        return e


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8080)
