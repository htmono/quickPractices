# Function named all_the_longest takes a list of strings as its argument.
# The function should return a new list containing the longest string in the original list.
# If more than one are equally long, the function should return all of the longest strings.

def all_the_longest(x):
    length = 0
    lista = []
    for y in x:
        if len(y) > length:
            length = len(y)
            # print(len(y))

    for y in x:
        if len(y) == length:
            lista.append(y)
            # print(lista)
    return lista


# Two tests:

my_list = ["first", "second", "fourth", "eleventh"]
result = all_the_longest(my_list)
print(result) # ['eleventh']

my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
result = all_the_longest(my_list)
print(result) # ['dorothy', 'richard']