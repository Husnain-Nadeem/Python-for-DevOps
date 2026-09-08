import sys
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

a=int(sys.argv[1])
operator=sys.argv[2]
b=int(sys.argv[3])

if operator == "+":
    result = add(a, b)
    print(f"The result of {a} + {b} is: {result}")
elif operator == "-":
    result = subtract(a, b)
    print(f"The result of {a} - {b} is: {result}")
elif operator == "*":
    result = multiply(a, b)
    print(f"The result of {a} * {b} is: {result}")
elif operator == "/":
    try:
        result = divide(a, b)
        print(f"The result of {a} / {b} is: {result}")
    except ValueError as e:
        print(e)    
        