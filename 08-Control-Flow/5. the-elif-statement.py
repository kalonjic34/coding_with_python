def positive_or_negative(number):
    if number >0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Neither, its zero"
    
print(positive_or_negative(5))
print(positive_or_negative(-1))
print(positive_or_negative(0))

def calculator(operation, a,b):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a -b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b
    else:
        return "Not sure what you want!"
    
print(calculator("add", 1, 5))
print(calculator("subtract", 3, 7))
print(calculator("multiply", 4, 3))
print(calculator("transmorgify", 2,2))