# read animals.txt
# and write animals_new.txt
with open('animals.txt') as animal_file:
    animals = animal_file.readlines()
    with open('animals_new.txt', 'w') as animal_new_file:
        for animal in animals:
            animal_new_file.write(animal.strip())
            animal_new_file.write(' ')
