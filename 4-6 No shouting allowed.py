# Write your solution here
def no_shouting(lista):
    newlist = []
    index = 0
    while index < len(lista):
        # print(lista[index])
        if lista[index].isupper() == False:
            print(lista[index])
            newlist.append(lista[index])
        index += 1

    return newlist






if __name__ == "__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)