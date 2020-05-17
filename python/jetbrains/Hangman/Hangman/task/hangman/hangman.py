import random


# Write your code here

def print_hidden_word(chosen, letters):
    print()
    for letter in chosen:
        if letter in letters:
            print(letter, end='')
        else:
            print("-", end='')
    print()


print("H A N G M A N")
word_list = ['python', 'java', 'kotlin', 'javascript']
chosen_word = random.choice(word_list)
tries = 8
identified_letters = set()
typed_letters = set()
hidden_word = "-" * len(chosen_word)
print_hidden_word(chosen_word, identified_letters)
previous_letter = ""
while tries != 0:

    letter = input("Input a letter: ")
    if not letter.islower():
        print("It is not an ASCII lowercase letter")
        print_hidden_word(chosen_word, identified_letters)
        continue
    if len(letter) != 1:
        print("You should print a single letter")
        print_hidden_word(chosen_word, identified_letters)
        continue
    if letter in typed_letters and letter not in identified_letters:
        print("You already typed this letter")
        print_hidden_word(chosen_word, identified_letters)
        continue

    if letter in chosen_word and letter not in identified_letters:
        identified_letters.add(letter)
    elif letter in identified_letters:
        tries -= 1
    elif letter not in chosen_word:
        print("No such letter in the word")
        tries -= 1
    elif identified_letters == set(chosen_word):
        tries -= 1
    else:
        typed_letters.add(letter)

    if identified_letters == set(chosen_word) and tries == 0:
        print("You guessed the word!")
        print("You survived!")
    elif identified_letters != set(chosen_word) and tries == 0:
        print("You are hanged!")
    else:
        print_hidden_word(chosen_word, identified_letters)
