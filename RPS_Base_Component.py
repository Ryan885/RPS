import random

# functions go here
def check_rounds():
    while True:
        response = input("How many rounds: ")

        round_error = "Please type either <enter> or an integer that is more than 0"

        # If infinite mode not chosen, check response
        # is an integer that is more than 0
        if response != "":
            try:
                response = int(response)

                # If response is too low, go back to
                # start of the loop
                if response < 1:
                    print(round_error)
                    continue

            # If response is not an integer go back to
            except ValueError:
                print(round_error)
                continue

        return response

def choice_checker(question, valid_list, error):

    valid = False
    while not valid:

        # Ask user for choice (and put choice in lowercase)
        response = input(question).lower()

        # iterates through list and if response is an item
        # in the list (or the first letter of an item), the
        # full item name is returned

        for item in valid_list:
            if response == item[0] or response == item:
                return item

        # output error
        print(error)
        print()

# Main routine goes here

# Lists of valid responses
yes_no_lists = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]

# Ask user if they have played before
# If 'no', show instructions


# ask user for # of rounds then loop...
rounds_played = 0
choose_instructions = "Please choose rock (r), paper (p) or scissors (s)"

# Ask user for # of rounds, <enter> for infinite mode
rounds = check_rounds()

end_game = "no"
while end_game == "no":

    # Start of game play loop
    # Rounds heading

    print()
    if rounds == "":
        heading = "Continuous Mode: Round {}".format(rounds_played + 1)
    else:
        heading = "Round {} of {}".format(rounds_played + 1, rounds)

    print(heading)
    choose_instructions = "Please choose rock (r), paper (p) or scissors (s) or 'xxx' to quit: "
    choose_error = "Please choose from rock / paper / scissors (or xxx to exit): "

    # Ask user for choice and check it is valid
    choose = choice_checker(choose_instructions, rps_list, choose_error)

    # End game if exit code is typed
    if choose == "xxx":
        break
    elif rounds == "":
        end_game = "no"
    elif rounds_played == rounds - 1:
        end_game = "yes"
    else:
        end_game = "no"
# rest of loop / game
    print("You chose {}".format(choose))
    rounds_played += 1




# ask user if they want to see their game history.
# if 'yes' show game history
