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
    looping = True
    firstName = input("What is your first name? >> ")
    lastName = input("What is your last name? >> ")
    user = BasicMathOperations(firstName, lastName)

    while looping == True:
        print("1: Greet user")
        print("2: Add two numbers")
        print("3: Perform operation on two numbers")
        print("4: Square a number")
        print("5: Compute a factorial")
        print("6: Count from one number to another")
        print("7: Calculate the hypotenuse of a right triangle")
        print("8: Calculate the area of a rectangle")
        print("9: Calculate the power of a number")
        print("10: Get the type of an input")
        print("0: exit program")
        inp = int(input("What would you like to do? >> "))

        if inp == 1:
            print(f"Hello {user.firstName} {user.lastName}!")
        elif inp == 2:
            num1 = int(input("What is your first number? >> "))
            num2 = int(input("What is your second number? >> "))
            print(user.sum(num1, num2))
        elif inp == 3:
            num1 = int(input("What is your first number? >> "))
            num2 = int(input("What is your second number? >> "))
            op = input("What is the operator you wish to use? (+, -, *, /) >> ")
            print(user.operation(num1, num2, op))
        elif inp == 4:
            num2 = int(input("What is your number? >> "))
            print(user.square(num1))
        elif inp == 5:
            num2 = int(input("What is your number? >> "))
            print(user.factorial(num1))
        elif inp == 6:
            num1 = int(input("What is your first number? >> "))
            num2 = int(input("What is your second number? >> "))
            print(user.count(num1, num2))
        elif inp == 7:
            num1 = int(input("What is the base? >> "))
            num2 = int(input("What is the height? >> "))
            print(user.calculateHypotenuse(num1, num2))
        elif inp == 8:
            num1 = int(input("What is the base? >> "))
            num2 = int(input("What is the height? >> "))
            print(user.areaRectangle(num1, num2))
        elif inp == 9:
            num1 = int(input("What is your first number? >> "))
            num2 = int(input("What is your second number? >> "))
            print(user.findPower(num1, num2))
        elif inp == 10:
            val = input("What is your variable to check? >> ")
            print(user.typeCheck(val))
        elif inp == 0:
            print("Goodbye!")
            looping == False
            break



main()