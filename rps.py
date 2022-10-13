# Rock Paper Scissor game from scratch.
import random

# Make list out of the possible choices player and computer can make
moves = ["rock", "paper", "scissors"]

# Set up a while-loop for game to continue as long as player wants it.
while True:

    # make variable for players pick and ask player for input
    playerChose = input("Which do you choose? (rock/paper/scissors \nIf you want to quit, you can type in 'quit' or 'q' ")

    # make variable for computer to pick
    computerChose = random.choice(moves)

    # Player can quit the game by typing out "quit" or "q"
    if playerChose == "quit" or playerChose == "q":
        break
    # deal with finding out the winner
    print(f"You chose {playerChose} and computer chose {computerChose}")
    if playerChose == computerChose:
        print("It's a tie!")
    if playerChose == "rock":
        if computerChose == "paper":
            print("Computer won!")
        elif computerChose == "scissors":
            print("You won!")

    if playerChose == "paper":
        if computerChose == "rock":
            print("You won!")
        elif computerChose == "scissors":
            print("Computer won!")

    if playerChose == "scissors":
        if computerChose == "rock":
            print("Computer won!")
        elif computerChose == "paper":
            print("You won!")
    # dotted lines for visibility
    print("-" * 10)
