import random
# To import the randomized numbers for the computer


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


# List of what the computer can choose to do in area / perimeter
advanced_math=["square", "rectangle", "triangle"]
units = ["mm", "cm", "m", "km"]

# Main Routine?
while True:
    try:
        # if I'm correct this should make comp_question generate random numbers for my random questions
        comp_number1 = (random.randrange(1, 10))
        comp_number2 = (random.randrange(1, 10))
        comp_number3 = (random.randrange(1, 10))

        # Area questions and Answer Method
        if want_question == "a":
            area_type = random.choice(advanced_math)
            unit_type = random.choice(units)

            if area_type == "square":
                print(f"The base of the square is {comp_number1} {unit_type}")
                answers = (comp_number1 * comp_number1)

            if area_type == "rectangle":
                print(f"The base of the rectangle is {comp_number1} {unit_type}, "
                      f"and the sides of the rectangle has a length of {comp_number2} {unit_type}")
                answers = (comp_number1 * comp_number2)

            if area_type == "triangle":
                print(f"The base of the triangle is {comp_number1} {unit_type}, "
                      f"and has the height of {comp_number2} {unit_type}")
                answers = int(round((comp_number1 * comp_number2 / 2)))

            user_choice = int(input(f"What is the area of the {area_type} in {unit_type} squared? "))

            if user_choice == answers:
                print("Correct!")
                break
            else:
                print(f"Incorrect the answer was {answers} {unit_type}²")

        # Perimeter Questions and Answer Method
        elif want_question == "p":
            area_type = random.choice(advanced_math)
            unit_type = random.choice(units)

            if area_type == "square":
                print(f"The base of the square is {comp_number1} {unit_type}")
                answers = (comp_number1 * 4)

            if area_type == "rectangle":
                print(f"The base of the rectangle is {comp_number1} {unit_type}, "
                      f"and the sides of the rectangle has a length of {comp_number2} {unit_type}")
                answers = (comp_number1 + comp_number2 * 2)

            if area_type == "triangle":
                print(f"The base of the triangle is {comp_number1} {unit_type}, "
                      f"and it's sides have the length of {comp_number2} {unit_type}, "
                      f"and {comp_number3} {unit_type}")
                answers = (comp_number1 + comp_number2 + comp_number3)

            user_choice = int(input(f"What is the perimeter of the {area_type} in {unit_type}? "))

            if user_choice == answers:
                print("Correct!")
                break
            else:
                print(f"Incorrect the answer was {answers} {unit_type}")

        elif want_question in ("+", "-", "*", "/"):
            user_choice = int(input(f"What is {comp_number1} {want_question} {comp_number2}? "))
            if want_question == '+':
                answers = (comp_number1 + comp_number2)
            if want_question == '-':
                answers = (comp_number1 - comp_number2)
            if want_question == '*':
                answers = (comp_number1 * comp_number2)
            if want_question == '/':
                answers = int(round((comp_number1 / comp_number2)))

            if user_choice == answers:
                print("Correct!")
                break
            else:
                print(f"Incorrect the answer was {answers}")

    except ValueError:
        print("Invalid Input")
        break
