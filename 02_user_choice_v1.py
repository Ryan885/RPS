# Functions
def choice_checker(question):

    error = "Please choose from rock / paper / scissors (or xxx to quit)"

    valid = False
    while not valid:

        # Ask user for choice (and put choice in lowercase)
        response = input(question).lower()

        if response == "rock" or response == "r":
            return response

        elif response == "paper" or response == "p":
            return response

        elif response == "scissors" or response == "s":
            return response

        elif response == "xxx":
            return response
        else:
            print(error)

# Main Routine Below

# Loop for testing purposes
user_choice = ""
while user_choice != "xxx":

    # Ask user for choice and check it's valid
    user_choice = choice_checker("Choose rock / paper / scissors (r/p/s): ")

    # Print out choice for comparison purposes
    print("You chose {}".format(user_choice))

