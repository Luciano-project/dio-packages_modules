# This is where we can find the simple arithmetic functions
from math import sqrt
import complement as cp
class Calculator:
    def __init__(self,number1,number2):
        self.num1 = number1
        self.num2 = number2

    def add(self):
        solution = self.num1 + self.num2
        res=cp.add(self.num1, self.num2)
        res[1]+=' {}'.format(solution)

        return res

    def subtract(self):
        solution = self.num1 - self.num2
        res = cp.subtract(self.num1, self.num2)
        res[1]+=' {}'.format(solution)

        return res

    def multiply(self):
        solution = self.num1 * self.num2
        res = cp.multiply(self.num1, self.num2)
        res[1]+=' {}'.format(solution)

        return res

    def divide(self):
        solution = self.num1 / self.num2
        res = cp.divide(self.num1, self.num2)
        res[1]+=' {}'.format(solution)

        return res

    def sqrt_op(self):
        solution = sqrt(self.num1)
        res = cp.sqrt_op(self.num1)
        res[1]+=' {}'.format(solution)

        return res

    def exponential(self):
        solution = self.num1**self.num2
        res = cp.exponential(self.num1, self.num2)
        res[1]+=' {}'.format(solution)

        return res