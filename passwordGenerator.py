# Project Python Password Generator
import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+']

print("Welcome to the Python Password Generator!")
totLetters = int(input("How many letters would you like in your password? "))
totSymbols = int(input("How many symbols  would you like in your password? "))
totNumbers = int(input("How many numbers would you like in your password? "))



myPassword = []                                  #for storing characters of the password

for password in range(0, totLetters):
    myPassword  += random.choice(letters)       # getting random letters from the list

for password in range(0,totSymbols):
    myPassword += random.choice(symbols)        # getting random symbols from the list


for password in range(0,totNumbers):
    myPassword += random.choice(numbers)        # getting random digits from the list


random.shuffle(myPassword)                     #shuffle the list to mixup the password

finalPassword = ""                             #converting list into string of characters

for characters in myPassword:
    finalPassword += characters

print(f"Here is your password: {finalPassword}")