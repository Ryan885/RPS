# Bad videos. Skipped over the entire first version of this.

def check_rounds():
    while True:
        response = input("How many rounds: ")

        round_error = "Please type either <enter> or an integer that is more than 0"
        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue

        return response


rounds_played = 0
choose_instructions = "Please choose rock (r), paper (p) or scissors (s)"

# Ask user for # of rounds, <enter> for infinite mode
rounds = check_rounds()

end_game = "no"
while end_game == "no":

    # 2:40 Looping Component Video
    print()
    if rounds == "":
        heading = "Continuous Mode: Round {}".format(rounds_played + 1)
    else:
        heading = "Round {} of {}".format(rounds_played + 1, rounds)

    print(heading)
    choose = input("{} or 'xxx' to  end: ".format(choose_instructions))

# End game if exit code is typed

    if choose == "xxx":
        break

# rest of loop / game
    print("You chose {}".format(choose))

    rounds_played += 1
    if rounds_played == rounds:
        break

print("Thank you for playing")
