def add(num1,num2):
    resolution="{} + {} =".format(num1, num2)
    return ["ADD",resolution]

def subtract(num1,num2):
    resolution = "{} - {} =".format(num1, num2)
    return ["SUBTRACT",resolution]

def multiply(num1,num2):
    resolution="{} * {} =".format(num1, num2)
    return ["MULTIPLY", resolution]

def divide(num1,num2):
    resolution="{} / {} =".format(num1, num2)
    return ["DIVIDE", resolution]

def sqrt_op(num1):
    resolution ="{}^(1/2) =".format(num1)
    return ["SQRT", resolution]

def exponential(num1,num2):
    resolution ="{}^{} =".format(num1, num2)
    return ["EXPONENTIAL", resolution]
