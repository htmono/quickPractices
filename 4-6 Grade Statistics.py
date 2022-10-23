# Write your solution here

# funktio joka kysyy exam pointsit + exercises
# splittaa ne
# laskee pisteet yhteen eli exam points + (muuta exercises) = yhteispisteet
# jos exam points on vähemmän kuin 10, automaattinen grade 0

# talleta arvo johonkin kuudesta grade-muuttujasta


points_average = 0
pass_percentage = 0


def main():
    # variables to store given grades
    grade0 = 0
    grade1 = 0
    grade2 = 0
    grade3 = 0
    grade4 = 0
    grade5 = 0
    sum_of_grades = 0
    sum_of_points = 0

    while True:
        user_input = input("Exam points and exercises completed: ")
        if user_input == "":
            break
        else:
            pisteet = user_input.split()
            exam_points = int(pisteet[0])
        # calculate exercise points: exercises completed * 0.1 and rounded to integer 0-10
        exercise_points = int(int(pisteet[1]) * 0.1)
        # Calculate the total points
        sum_of_points = sum_of_points + exam_points + exercise_points
        if exam_points < 10:
            grade0 += 1
        else:
            total_points = exam_points + exercise_points

            grade = total_points
            sum_of_grades = sum_of_grades + total_points

            # count the number of grades
            if grade <= 14:
                grade0 += 1
            elif grade >= 15 and grade < 18:
                grade1 += 1
            elif grade >= 18 and grade < 21:
                grade2 += 1
            elif grade >= 21 and grade < 24:
                grade3 += 1
            elif grade >= 24 and grade < 28:
                grade4 += 1
            elif grade >= 28 and grade <= 30:
                grade5 += 1

    statistics(grade0, grade1, grade2, grade3, grade4, grade5, sum_of_points)


def statistics(grade0, grade1, grade2, grade3, grade4, grade5, x):
    # pass_percentage =
    print("Statistics: ")
    print(f"Points average: {x / (grade0 + grade1 + grade2 + grade3 + grade4 + grade5):.1f}")
    print(
        f"Pass percentage: {((grade1 + grade2 + grade3 + grade4 + grade5) / (grade0 + grade1 + grade2 + grade3 + grade4 + grade5)) * 100:.1f}")
    print("Grade distribution:")
    print(f"5: {'*' * grade5}")
    print(f"4: {'*' * grade4}")
    print(f"3: {'*' * grade3}")
    print(f"2: {'*' * grade2}")
    print(f"1: {'*' * grade1}")
    print(f"0: {'*' * grade0}")

# NOT USED
# Main function calls this to convert two user inputs into total points
# def convert(lista):
#    exam_points = int(lista[0])
#    # calculate exercise points: exercises completed * 0.1 and rounded to integer 0-10
#    exercise_points = int(int(lista[1]) * 0.1)
#    # Calculate the total points
#    if exam_points < 10:
#        total_points = 0
#    else:
#        total_points = exam_points + exercise_points
#
#    return(total_points)


# run the main function
main()

