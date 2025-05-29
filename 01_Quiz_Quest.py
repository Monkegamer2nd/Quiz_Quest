import random

# functions go here

# Check that users have entered a valid
# option based on a list
def string_checker(question, valid_ans=("yes", "no")):

    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        # Get user response and make sure it's lowercase
        users_response = input(question).lower()

        for item in valid_ans:
            # check if the user response is a word in the list
            if item == users_response:
                return item

            # check if the user response is the same as
            # the first letter of an item in the list
            elif users_response == item[0]:
                return item

        # print error if user does not enter something that is valid
        print(error)
        print()

# Displays instructions
def instructions():
    """Prints instructions"""

    print("""
*** Instructions ***

To begin, choose the number of questions you want (or press <enter> for infinite mode).

Then the computer will generate the mathematical questions for you to answer

*** Formula List! (for area & perimeter) ***

o   Square: Area = base * base. Perimeter = base + base + base + base 

o   Rectangle: Area = base * length. Perimeter = base + base + length + length 

o   Triangle: Area = base * height / 2. Perimeter = base + side 1 + side 2

Make sure to round your answers!

press <xxx> to end the game when it asks for a type of question.

Good Luck!
    """)

# checks for anm integer more than 0 (allows <enter>)
def int_check(question):
    while True:
        error = "please enter an integer more than / equal to 1."

        to_check = input(question)

        # check for infinite mode
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            # checks that the number is more than / equal to 1
            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

# to check the question
def question_check(question):
    while True:
        error = "please enter an integer no floats/strings."

        to_check = input(question)

        try:
            response = int(to_check)

            return response

        except ValueError:
            print(error)

# To get what kind of question the user wants
def question_type(question, valid_ans=("+", "-", "*", "/", "area", "perimeter", "xxx")):

    error = f"Please enter a valid answer from the following list {valid_ans}"

    while True:

        # to get the user's input and make sure that it's lower
        response = input(question).lower()

        for item in valid_ans:
            # check if the user response is a word in the list
            if item == response:
                return item

            # check if the user response is the same as
            # the first letter of an item in the list
            elif response == item[0]:
                return item

        print(error)
        print()

# compares user to the answer and returns
# result (win / lose )
def quiz_compare(guess, quiz_answer):

    # If the user and the computer choice is the same, it's a tie
    if guess == quiz_answer:
        round_result = "win"

    # if it's not a win then it's a loss
    else:
        round_result = "lose"

    return round_result


# Initialise game variables
mode = "regular"

rounds_played = 0
rounds_lost = 0

game_history = []

# Main routine
print()
print("➕➖✖️➗ Quiz Quest ➕➖✖️➗")
print()

# ask the user if they want tp see the instructions and display
# them if requested
want_instructions = string_checker("Do you want to see the instructions? ")

# checks users enter yes (y) or no (n)
if want_instructions == "yes":
    instructions()

# Instructions

# Ask user for number rounds / infinite mode
num_rounds = int_check("How many rounds would you like? Push <enter> for infinite mode: ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5


# List of what the computer can choose to do in area / perimeter
advanced_math = ["square", "rectangle", "triangle"]
units = ["mm", "cm", "m", "km"]

# Game loop starts here
while rounds_played < num_rounds:

    # Rounds headings (based on mode)
    if mode == "infinite":
        rounds_heading = f"\n♾️♾️♾️ Round {rounds_played + 1} (Infinite Mode) ♾️♾️♾️"
    else:
        rounds_heading = f"\n💿💿💿 Round {rounds_played + 1} of {num_rounds} 💿💿💿"

    print(rounds_heading)
    print()

    # Asks the user a question for their question
    want_question = question_type("What kind of math-based question would you like? ")


    # if I'm correct this should make comp_question generate random numbers for my random questions
    comp_number1 = (random.randrange(1, 50))
    comp_number2 = (random.randrange(1, 50))
    comp_number3 = (random.randrange(1, 50))

    # Area questions and Answer Method
    if want_question == "area":
        area_type = random.choice(advanced_math)
        unit_type = random.choice(units)

        if area_type == "square":
            questions = f"The base of the square is {comp_number1} {unit_type}"
            quiz_answer = (comp_number1 * comp_number1)

        if area_type == "rectangle":
            questions = (f"The base of the rectangle is {comp_number1} {unit_type}, "
                  f"and the sides of the rectangle has a length of {comp_number2} {unit_type}")
            quiz_answer = (comp_number1 * comp_number2)

        if area_type == "triangle":
            questions = (f"The base of the triangle is {comp_number1} {unit_type}, "
                  f"and has the height of {comp_number2} {unit_type}")
            quiz_answer = int(round((comp_number1 * comp_number2 / 2)))

        print()
        print(questions)
        guess = question_check(f"What is the area of the {area_type} in {unit_type} squared? ")

        results = quiz_compare(guess, quiz_answer)

        if results == "lose":
            feedback = f"Incorrect, the answer was {quiz_answer} {unit_type}²"
            rounds_lost += 1
        else:
            feedback = "Correct!"

        round_feedback = f"{questions}: you were {feedback}"
        history_item = f"Question: {rounds_played + 1} - Was {round_feedback}"
        print()
        print(round_feedback)
        game_history.append(history_item)

        # increase number of rounds played
        rounds_played += 1

        # if users are in infinite mode, increase number of rounds
        if mode == "infinite":
            num_rounds += 1

    # Perimeter Questions and Answer Method
    elif want_question == "perimeter":
        area_type = random.choice(advanced_math)
        unit_type = random.choice(units)

        if area_type == "square":
            questions = f"The base of the square is {comp_number1} {unit_type}"
            quiz_answer = (comp_number1 * 4)

        if area_type == "rectangle":
            questions = (f"The base of the rectangle is {comp_number1} {unit_type}, "
                         f"and the sides of the rectangle has a length of {comp_number2} {unit_type}")
            quiz_answer = (comp_number1 + comp_number2 + comp_number1 + comp_number2)

        if area_type == "triangle":
            questions = (f"The base of the triangle is {comp_number1} {unit_type}, "
                         f"and it's sides have the length of {comp_number2} {unit_type}, "
                         f"and {comp_number3} {unit_type}")
            quiz_answer = (comp_number1 + comp_number2 + comp_number3)

        print()
        print(questions)
        guess = question_check(f"What is the perimeter of the {area_type} in {unit_type}? ")

        results = quiz_compare(guess, quiz_answer)

        if results == "lose":
            feedback = f"Incorrect, the answer was {quiz_answer} {unit_type}"
            rounds_lost += 1
        else:
            feedback = "Correct!"

        round_feedback = f"{questions}: you were {feedback}"
        history_item = f"Question: {rounds_played + 1} - Was {round_feedback}"
        print()
        print(round_feedback)
        game_history.append(history_item)

        # increase number of rounds played
        rounds_played += 1

        # if users are in infinite mode, increase number of rounds
        if mode == "infinite":
            num_rounds += 1

    elif want_question in ("+", "-", "*", "/"):
        questions = f"{comp_number1} {want_question} {comp_number2}"
        if want_question == '+':
            quiz_answer = (comp_number1 + comp_number2)
        if want_question == '-':
            quiz_answer = (comp_number1 - comp_number2)
        if want_question == '*':
            quiz_answer = (comp_number1 * comp_number2)
        if want_question == '/':
            quiz_answer = int(round((comp_number1 / comp_number2)))

        print()
        print(questions)
        guess = question_check(f"What does it equal? ")

        results = quiz_compare(guess, quiz_answer)

        if results == "lose":
            feedback = f"Incorrect, the answer was {quiz_answer} ❌"
            rounds_lost += 1
        else:
            feedback = "Correct! ✅"

        round_feedback = f"{questions}: you were {feedback}"
        history_item = f"Question: {rounds_played + 1} - Was {round_feedback}"
        print()
        print(round_feedback)
        game_history.append(history_item)

        # increase number of rounds played
        rounds_played += 1

        # if users are in infinite mode, increase number of rounds
        if mode == "infinite":
            num_rounds += 1

    # if users are in infinite mode, or want to finish a game they can use this to break out of the loop.
    elif want_question == "xxx":
        break


if rounds_played > 0:
    # Calculate Statistics
    rounds_won = rounds_played - rounds_lost
    percent_won = rounds_won / rounds_played * 100
    percent_lost = rounds_lost / rounds_played * 100

    # Output Game Statistics
    print()
    print("📊📊📊 Game Statistics 📊📊📊")
    print(f"👍 Won: {percent_won:.2f} \t "
          f"👎 Lost: {percent_lost:.2f} \t")

    # ask user if they want to see their game history and output if requested
    see_history = string_checker("\nDo you want to see your game history? ")
    if see_history == "yes":
        for item in game_history:
            print(item)

    print()
    print("Thanks for playing.")
else:
    print("You chickened out! 🐔🐔🐔")