def addition(a, b):
    a= int(a)
    b= int(b)
    c= b + a
    return c

def subtraction(a, b):
    a= int(a)
    b= int(b)
    c= b - a
    return c

def multiplication(a, b):
    a= int(a)
    b= int(b)
    c= a * b
    return c

def division(a, b):
    a= int(a)
    b= int(b)
    c= a / b
    return c

def square(a):
    return a**2

def squareroot(a):
    return a**(1/2)

class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    def squared(self, a):
        self.result = square(a)
        return self.result

    def squarerooted(self, a):
        self.result = squareroot(a)
        return self.result

