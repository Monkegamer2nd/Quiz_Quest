import random
from re import error


# To get what kind of question the user wants
def question_type(question, valid_ans=("+", "-", "*", "/", "a", "p")):

    error = f"Please enter a valid answer from the following list {valid_ans}"

    while True:

        # to get the user's input and make sure that it's lower
        user_response = input(question).lower()

        for item in valid_ans:
            if item == user_response:
                return item

            elif user_response == item[0]:
                return item

        if user_response == "a":
            return "area"
        elif user_response == "p":
            return "perimeter"

        print(error)
        print()



# Asks the user a question for their question
want_question = question_type("What kind of math-based question would you like? ")

# if I'm correct this should make comp_question generate random numbers for my random questions
comp_number1 = (random.randrange(1,10))
comp_number2 = (random.randrange(1,10))
comp_number3 = (random.randrange(1, 10))

# List of what the computer can choose to do in area / perimeter
advanced_math=["square", "rectangle", "triangle"]
units = ["mm", "cm", "m", "km"]
while True:
    try:
        if want_question == "a":
            area_type = random.choice(advanced_math)
            unit_type = random.choice(units)

            if area_type == "square":
                print(f"The base of the square is {comp_number1} {unit_type}")
                answer = (comp_number1 * comp_number1)

            if area_type == "rectangle":
                print(f"The base of the rectangle is {comp_number1} {unit_type}, "
                      f"and the sides of the rectangle has a length of {comp_number2} {unit_type}")
                answer = (comp_number1 * comp_number2)

            if area_type == "triangle":
                print(f"The base of the triangle is {comp_number1} {unit_type}, "
                      f"and has the height of {comp_number2} {unit_type}")
                answer = (comp_number1 * comp_number2 / 2)

            user_choice = input(f"What is the area of the {area_type} in {unit_type} squared? ")

            user_choice = int(user_choice)

            if user_choice == answer:
                print("Correct!")
                break
            else:
                print(f"Incorrect the answer was {answer} {unit_type}")

    except ValueError:
        print("Invalid Response.")
        break

    try:
        if want_question == "p":
            area_type = random.choice(advanced_math)
            unit_type = random.choice(units)

            if area_type == "square":
                print(f"The base of the square is {comp_number1} {unit_type}")
                answer = (comp_number1 * 4)

            if area_type == "rectangle":
                print(f"The base of the rectangle is {comp_number1} {unit_type}, "
                      f"and the sides of the rectangle has a length of {comp_number2} {unit_type}")
                answer = (comp_number1 + comp_number2 * 2)

            if area_type == "triangle":
                print(f"The base of the triangle is {comp_number1} {unit_type}, "
                      f"and it's sides have the length of {comp_number2} {unit_type}, "
                      f"and {comp_number3} {unit_type}")
                answer = (comp_number1 + comp_number2 + comp_number3)

            user_choice = int(input(f"What is the perimeter of the {area_type} in {unit_type}? "))

            if user_choice == answer:
                print("Correct!")
                break
            else:
                print(f"Incorrect the answer was {answer} {unit_type}")

    except ValueError:
        print("Invalid Response.")
        break

    try:
        user_choice = int(input(f"what is {comp_number1} {want_question} {comp_number2} "))
        if want_question == '+':
            answer = (comp_number1 + comp_number2)
            if want_question == '-':
                answer = (comp_number1 - comp_number2)
                if want_question == '*':
                    answer = (comp_number1 * comp_number2)
                    if want_question == '/':
                        answer = (comp_number1 / comp_number2)

            if user_choice == answer:
                print("Correct!")
                break
            else:
                print(f"Incorrect the answer was {answer}")

    except ValueError:
        print("Invalid Response.")
        break