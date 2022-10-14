# Write your solution here
# You can test your function by calling it within the following block

def spruce(x):
    index = x - 1
    stars = "*"
    star_index = 1
    print("a spruce!")
    while index >= 0:
        print((index * " ") + (stars * star_index))
        index -= 1
        star_index += 2
    jalka = "*"
    print(" " * ((star_index // 2) - 1) + jalka)



if __name__ == "__main__":
    spruce(5)