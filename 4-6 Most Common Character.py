# Write your solution here
def most_common_character(text):
    yleisin = text[0]

    for y in text:
        if text.count(y) > text.count(yleisin):
            yleisin = y

    return yleisin



if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))