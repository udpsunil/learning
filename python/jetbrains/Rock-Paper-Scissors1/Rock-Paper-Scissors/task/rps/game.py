import random


# Write your code here

def points(x):
    if x > 0:
        return 100
    elif x == 0:
        return 50
    else:
        return 0


name = input("Enter you name:")
print("Hello, {}".format(name))
user_score = 0
with open('rating.txt', 'r') as rating_file:
    for line in rating_file.readlines():
        if name in line:
            user_score = int(line.split(' ')[1])
            break
rps_choice_inputs = input()
if len(rps_choice_inputs) == 0:
    rps_choices = ['rock', 'paper', 'scissors']
else:
    rps_choices = rps_choice_inputs.split()
print("Okay, let's start")
messages = ['Well done. Computer chose {} and failed',
            'There is a draw ({})',
            'Sorry, but computer chose {}']

num_of_choices = len(rps_choices)
half_of_choices = num_of_choices // 2
score_updates = [points(x) for x in range(half_of_choices, -half_of_choices - 1, -1)]
user_input = input()
while user_input.find('!exit') == -1:
    if user_input in ['!rating']:
        print("Your rating: {}".format(user_score))
    if user_input not in rps_choices:
        print("Invalid input")
    else:
        user_index = rps_choices.index(user_input)
        computer_choice = random.choice(rps_choices)
        game_outcome = [(rps_choices.index(computer_choice) + x) % num_of_choices for x in
                        range(half_of_choices, -half_of_choices - 1, -1)]
        user_score += score_updates[game_outcome.index(user_index)]
        print(messages[game_outcome.index(user_index)].format(computer_choice))
    user_input = input()
else:
    print("Bye!")
