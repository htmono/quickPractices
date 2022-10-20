
# Function "shortest" takes a list of strings as its argument.
# The function returns whichever of the strings is the shortest.

def shortest(x):
    longest = 0
    for y in x:
        if len(y) > longest:
            longest = len(y)
    text = ""
    for y in x:
        # print(len(y))
        if len(y) < longest:
            text = y
            longest = len(y)

    return text

# Test:
my_list = ["first", "second", "fourth", "eleventh"]
result = shortest(my_list)
print(result)