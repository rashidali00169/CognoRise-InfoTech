#CognoRise InfoTech Internship
#Task 2
#project Calculator

firstNumber = int(input("Enter first number: "))
operator = input("Enter Operator from given below:\n'+'\n'-'\n'*'\n'/'\n'%'\n ")
secondNumber = int(input("Enter second number: "))

result = 0
def sum(num1,num2):
    result = num1 + num2
    return result

def subtract(num1,num2):
    result = num1 - num2
    return result
def multiply(num1,num2):
    result = num1 * num2
    return result

def divide(num1,num2):
    result = num1 / num2
    return result

def modulus(num1,num2):
    result = num1 % num2
    return result

#def myCalculator():
if (operator == '+'):
    result = sum(firstNumber,secondNumber)
    print(f"Answer is: {result}")

elif (operator == '-'):
    result =subtract(firstNumber,secondNumber)
    print(f"Answer is: {result}")
elif (operator == '*'):
    result = multiply(firstNumber,secondNumber)
    print(f"Answer is: {result}")
elif (operator == '/'):
    result = divide(firstNumber,secondNumber)
    print(f"Answer is: {result}")
elif (operator == '%'):
    result = modulus(firstNumber,secondNumber)
    print(f"Answer is: {result}")
else:
    print("Enter a valid operator from the given operators")