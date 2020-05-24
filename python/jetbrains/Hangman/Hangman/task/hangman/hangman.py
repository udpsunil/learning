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

while True:
    menu = input('Type "play" to play the game, "exit" to quit: ')
    if menu == 'exit':
        exit()
    elif menu == 'play':
        break
    else:
        continue

print_hidden_word(chosen_word, identified_letters)

while tries != 0:

    letter = input("Input a letter: ")
    if letter in set(chosen_word):
        if letter in identified_letters:
            print("You already typed this letter")
        else:
            identified_letters.add(letter)
    elif len(letter) > 1:
        print("You should print a single letter")
    elif not letter.islower():
        print("It is not an ASCII lowercase letter")
    elif letter not in set(chosen_word) and letter not in typed_letters:
        print("No such letter in the word")
        typed_letters.add(letter)
        tries -= 1
    elif letter in typed_letters and tries >= 1:
        print("You already typed this letter")
    else:
        typed_letters.add(letter)
        tries -= 1

    if tries == 0:
        if len(identified_letters) == len(set(chosen_word)):
            print("You survived!")
        else:
            print("You are hanged!")
        break

    print_hidden_word(chosen_word, identified_letters)
