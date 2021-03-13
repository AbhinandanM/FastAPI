# FastAPI
## Quickstart
```
git clone 
cd FastAPI
pip install requirements.txt
cd test&modules/modules
**Run** python maths.py/strings.py
```
## Running Tests.
Tests for this project are defined in the tests&modules/ folder.
This project uses unittest to define tests. 
```
cd test&modules
**Run** python test_maths.py/test_strings.py
```
## Project Tree
```
FastAPI
├───tests&modules
│   ├───modules
|   |   ├────maths.py
|   |   ├────strings.py
│   │   └───__pycache__
│   ├────test_maths.py
│   ├────test_strings.py
│   └───__pycache__
└───requirements.txt
```
## Sample request to calculate and return nth Fibonacci (n > 1 < 100).
```
http://Domain/returnFibonacci/?n=9
```
## Sample request to calculate and return the factorial of a given number.
```
http://Domain/returnFactorial/?n=9
```
## Sample request to calculate and return the length of a string.
```
http://Domain/strings/getLenOfString/?string=I-am-a-string
```
## Sample request to generate and return a string of a given length of a chosen character as input.
```
http://Domain/strings/generateString/?char=f&count=10
```
