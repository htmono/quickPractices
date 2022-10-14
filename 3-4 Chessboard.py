# Create a chessboard out of ones and zeroes. Function takes and integer argument
# which specifies the length of the side of the board.

def chessboard(size):
    index = 0
    while index < size:
        if index % 2:
            if size % 2:
                print("01" * (size // 2) + "0")
            else:
                print("01" * (size // 2))
        else:
            if size % 2:
                print("10" * (size // 2) + "1")
            else:
                print("10" * (size // 2))
        index += 1


# Testing the function
if __name__ == "__main__":
    chessboard(3)
