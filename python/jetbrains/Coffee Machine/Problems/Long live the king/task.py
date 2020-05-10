x_coord = int(input())
y_coord = int(input())

num_of_moves = 0

if 2 <= x_coord <= 7:
    num_of_moves += 2
    num_of_moves += 6 if 2 <= y_coord <= 7 else 3
else:
    num_of_moves += 1
    num_of_moves += 4 if 2 <= y_coord <= 7 else 2
print(num_of_moves)
