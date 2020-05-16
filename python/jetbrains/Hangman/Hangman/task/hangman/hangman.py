import random

# Write your code here
print("H A N G M A N")
word_list = ['python', 'java', 'kotlin', 'javascript']
chosen_word = random.choice(word_list)

word = input("Guess the word {}: ".format(chosen_word[:3]+(len(chosen_word)-3)*'-'))
if word == chosen_word:
    print("You survived!")
else:
    print("You are hanged!")
