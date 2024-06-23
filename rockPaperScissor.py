
#Project
#Rock, Paper, Scisso Game

import random

rock = ''' ROCK
    _________
___|     _____)
        (_____)
        (______)
---      (____)
  |_____(___)

'''


paper = ''' PAPER
    ____________
___|     __________)
        (____________)
        (______________)
---     (__________)
  |_____(________)

'''


scissor = ''' SCISSOR
    _______
___|  _____ )______
         __________ )
           __________
        _____________ )
        (_____)
---|___(___)

'''

print(rock)
print(paper)
print(scissor)

#Rules for the game
print("Game Rules:")
print("Rock crushes Scissors")
print("Scissors cut Paper")
print("Paper wraps Rock\n")


# 0 for Rock
# 1 for paper
# 2 for scissor

computerChoice = random.randint(0,2)


myChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissor: "))

print(f"Computer Choose {computerChoice}")
print(f"You choose {myChoice}")

if (myChoice >= 3 or myChoice <0):
    print("Give a valid number from [0, 1, 2]")
elif(myChoice == computerChoice):
    print("Draw")
#checking all conditions for my winning
elif((myChoice == 0) and (computerChoice == 2 )) or ((myChoice == 2) and (computerChoice == 1)) or ((myChoice == 1) and (computerChoice == 0)):  #Rock wins against scissor
    print("You Win")

else:
    print("Computer Win")


playAgain = input("Do you want to play again? Type 'Y' for YES and 'N' for NO: ")

while (playAgain == 'y' or playAgain == 'Y'):

    computerChoice = random.randint(0, 2)

    myChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissor: "))

    print(f"Computer Choose {computerChoice}")
    print(f"You choose {myChoice}")

    if (myChoice >= 3 or myChoice < 0):
        print("Give a valid number from [0, 1, 2]")
    elif (myChoice == computerChoice):
        print("Draw")
    # checking all conditions for my winning
    elif ((myChoice == 0) and (computerChoice == 2)) or ((myChoice == 2) and (computerChoice == 1)) or (
            (myChoice == 1) and (computerChoice == 0)):  # Rock wins against scissor
        print("You Win")

    else:
        print("Computer Win")

    playAgain = input("Do you want to play again? Type 'Y' for YES and 'N' for NO: ")

