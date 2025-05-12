# *******************************
# * Name: Quiz Quest            *
# * Author: Talon               *
# * Date: 13/05/2025            *
# * Purpose: Be able to com-    *
# * -plete a math quiz with     *
# * computer generated questions*
# *******************************

# functions go here

# Check that users have entered a valid
# option based on a list
def string_checker(question, valid_ans=("yes", "no")):

    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        # Get user response and make sure it's lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # check if the user response is a word in the list
            if item == user_response:
                return item

            # check if the user response is the same as
            # the first letter of an item in the list
            elif user_response == item[0]:
                return item

        # print error if user does not enter something that is valid
        print(error)
        print()


# Displays instructions

def instructions():
    """Prints instructions"""

    print("""
*** Instructions ***

To begin, choose the number of questions (or press <enter> for infinite mode).

Then the computer will generate the mathematical question for you to answer

press <xxx> to end the game at anytime.

Good Luck!
    """)


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

print("Program continues")