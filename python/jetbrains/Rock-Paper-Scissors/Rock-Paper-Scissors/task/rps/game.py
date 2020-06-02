# Write your code here
rps_choices = ['rock', 'paper', 'scissors']
user_input = input()
computer_choice = rps_choices[(rps_choices.index(user_input) + 1)%3]
print("Sorry, but computer chose {}".format(computer_choice))

