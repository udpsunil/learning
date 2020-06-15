import random
# Write your code here
rps_choices = ['rock', 'paper', 'scissors']
messages = ['Well done. Computer chose {} and failed',
            'There is a draw ({})',
            'Sorry, but computer chose {}']
user_input = input()
while user_input.find('!exit') == -1:
    if user_input not in rps_choices:
        print("Invalid input")
        continue
    else:
        user_index = rps_choices.index(user_input)
        computer_choice = random.choice(rps_choices)

        game_outcome =[(rps_choices.index(computer_choice) + 1) % 3,
                       rps_choices.index(computer_choice),
                       (rps_choices.index(computer_choice) - 1) % 3]

        print(messages[game_outcome.index(user_index)].format(computer_choice))
        user_input = input()
else:
    print("Bye!")
