# Rock Paper Scissor game from scratch.
import random

# Make list out of the possible choices player and computer can make
moves = ["rock", "paper", "scissors"]

# make variable for players pick and ask player for input
pcChoose = input("Which do you choose? (rock/paper/scissors ")
# make variable for computer to pick
opChoose = random.choice(moves)

# deal with finding out the winner
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