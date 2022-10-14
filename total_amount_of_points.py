# Calculate the score of team from list. Each "game"  is represented by a string in the format "x:y",
# where x is our team's score and y is our opponents score.
# 3 points are awarded for a win(x>y), 0 points for loss(x<y) and 1 point for a tie.

def points(games):
    index = 0
    place = 0
    score = 0
    while index < len(games):

        splitattu = games[index].split(":")
        # print(splitattu)
        if splitattu[0] > splitattu[1]:
            score = score + 3
        elif splitattu[0] == splitattu[1]:
            score = score + 1

        index += 1
    return(score)

# test cases
print(points(['1:0', '2:0', '3:0', '4:0', '2:1', '3:1', '4:1', '3:2', '4:2', '4:3'])) # 30 points
print(points(['1:1','2:2','3:3','4:4','2:2','3:3','4:4','3:3','4:4','4:4'])) # 10 points