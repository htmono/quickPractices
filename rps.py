# Rock Paper Scissor game from scratch.
import random

# Make list out of the possible choices player and computer can make
moves = ["rock", "paper", "scissors"]

playerScore = 0
computerScore = 0


# Set up a while-loop for game to continue as long as player wants it.
while True:

    # make variable for players pick and ask player for input
    print("If you want to quit, you can type in 'quit' or 'q' ")
    playerChose = input("Which do you choose? (rock/paper/scissors ")


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
            computerScore += 1
        elif computerChose == "scissors":
            print("You won!")
            playerScore += 1

    if playerChose == "paper":
        if computerChose == "rock":
            print("You won!")
            playerScore += 1
        elif computerChose == "scissors":
            print("Computer won!")
            computerScore += 1

    if playerChose == "scissors":
        if computerChose == "rock":
            print("Computer won!")
            computerScore += 1
        elif computerChose == "paper":
            print("You won!")
            playerScore += 1
    # dotted lines for visibility
    print("-" * 10)

# Check who won the game
if playerScore > computerScore:
    winner = "You"
elif playerScore < computerScore:
    winner = "Computer"
else:
    winner = 0

if winner == 0:
    print (f"You got {playerScore} points and computer got {computerScore} points. It's a tie!")
else:
    print(f"You got {playerScore} points and computer got {computerScore} points. {winner} won!")
