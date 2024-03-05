import math

class BasicMathOperations:
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname

    def sum(self, num1, num2):
        return num1+num2
    
    def operation(self, num1, num2, operator):
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == "/":
            return num1 / num2
        
    def square(self, num):
        return num ** 2

    def factorial(self, num):
        return math.factorial(num)
    
    def count(self, num1, num2):
        countNums = []
        for i in range(num1, num2):
            countNums.append(i)
        return countNums
    
    def calculateHypotenuse(self, num1, num2):
        base = self.square(num1)
        height = self.square(num2)
        hypoSquared = base + height
        return hypoSquared ** 0.5
    
    def areaRectangle(self, num1, num2):
        return num1 * num2
    
    def findPower(self, num1, num2):
        return num1 ** num2
    
    def typeCheck(self, var):
        return type(var)
    

def main():
    firstName = input("What is your first name? >> ")
    lastName = input("What is your last name? >> ")
    user = BasicMathOperations(firstName, lastName)

    print(user.sum(2,3))
    print(user.operation(3,4,'*'))
    print(user.square(3))
    print(user.factorial(5))
    print(user.count(14, 22))
    print(user.calculateHypotenuse(2,3))
    print(user.areaRectangle(6,8))
    print(user.findPower(4,3))
    print(user.typeCheck("hello!"))

main()