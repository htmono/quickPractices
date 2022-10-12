# Rock Paper Scissor game from scratch.
import random
# assign rock, paper and scissors as values
rock = 1
paper = 2
scissors = 3

# Make computer choose one of three randomly (import random first?)
moves = ["rock", "paper", "scissors"]
opChoose = random.choice(moves)

# make variable for players pick and ask player for input
pcChoose = input("Which do you choose? (rock/paper/scissors ")

# deal with assigning a winner

print(f"You chose {pcChoose} and computer chose {opChoose}")
if pcChoose == opChoose:
    print("It's a tie!")
if pcChoose == "rock":
    if opChoose == "paper":
        print("Computer won!")
    elif opChoose == "scissors":
        print("You won!")

if pcChoose == "paper":
    if opChoose == "rock":
        print("You won!")
    elif opChoose == "scissors":
        print("Computer won!")

if pcChoose == "scissors":
    if opChoose == "rock":
        print("Computer won!")
    elif opChoose == "paper":
        print("You won!")