# Please write a function named everything_reversed,
# which takes a list of strings as its argument. The function
# returns a new list with all of the items on the original
# list reversed. Also the order of items should be reversed
# on the new list.

# Write your solution here

def everything_reversed(x):
    lista = []

    for y in x:
        lista.append(y[::-1])
    return lista[::-1]


# Test
if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)  # ['erom eno', 'elpmaxe', 'ereht', 'iH']