# Write your solution here

# Function "squared" takes string and integer argument and prints out
# a square of characters.

def squared(text, x):
    index = 0
    helper = 0
    while index < x:
        rivi = text * x * x
        print(rivi[helper:helper + x])
        index += 1
        helper = helper + x


# Testing the function
if __name__ == "__main__":
    squared("ab", 5)