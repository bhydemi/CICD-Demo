def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Denominator cannot be zero")
    return a / b

if __name__ == "__main__":
    print(add(5, 3))        # Output: 8
    print(subtract(5, 3))   # Output: 2
    print(multiply(5, 3))   # Output: 15