# Rock Paper Scissor game from scratch.
import random

# Make list out of the possible choices player and computer can make
moves = ["rock", "paper", "scissors"]

# Set up a while-loop for game to continue as long as player wants it.
while True:

# make variable for players pick and ask player for input
    pcChoose = input("Which do you choose? (rock/paper/scissors \nIf you want to quit, you can type in 'quit' or 'q' ")

# make variable for computer to pick
    opChoose = random.choice(moves)

# Player can quit the game by typing out "quit" or "q"
    if pcChoose == "quit" or pcChoose == "q":
        break
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