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

    # Start of Game Play Loop

    # Rounds heading
    print()
    if rounds == "":
        heading = "Continuous Mode: Round {}".format(rounds_played)
        print(heading)
        choose = input("{} or 'xxx' to  end: ".format(choose_instructions))
        if choose == "xxx":
            break
    else:
        heading = "Round {} of {}".format(rounds_played + 1, rounds)
        print(heading)
        choose = input(choose_instructions)
        if rounds_played == rounds - 1:
            end_game = "yes"

# rest of loop / game
    print("You chose {}".format(choose))

    rounds_played += 1



# ask user if they want to see their game history.
# if 'yes' show game history
