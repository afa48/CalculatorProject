def addition(a, b):
    return int(a) + int(b)

def subtraction(a, b):
    return int(b) - int(a)

def multiplication(a, b):
    a= int(a)
    b= int(b)
    c= a * b
    return c

def division(a, b):
    a= int(a)
    b= int(b)
    c= b / a
    return c

def square(a):
    a= int(a)
    c= a**2
    return c

def squareroot(a):
    a= float(a)
    c= a**(1/2)
    return c

class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        print("add: ", self.result)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        print("subtract: ", self.result)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        print("multiply: ", self.result)
        return self.result

    def divide(self, a, b):
        self.result = division(a, b)
        if int (b) !=  0:
            return round((float (b) / float (a)),9)
        else:
            return 'error, divisor y can not be zero'

    def squared(self, a):
        self.result = str(square(a))
        print("squared: ", self.result)
        return self.result

    def squarerooted(self, a):
        self.result = round(squareroot(a), 10)
        #new_result = round(self.result, 9)
        formatted_string = "{:.9}".format(self.result)
        #float_value = float(formatted_string)
        return formatted_string

