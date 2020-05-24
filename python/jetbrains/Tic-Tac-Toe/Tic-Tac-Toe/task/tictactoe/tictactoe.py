# write your code here
def print_ttt(ttt):
    print(9 * "-")
    for index in range(0, len(ttt), 3):
        print("| " + " ".join(list(ttt[index: index + 3])) + " |")
    print(9 * "-")


def game_not_finished(l):
    if abs(l.count('X') - l.count('O')) not in [0, 1]:
        print("Impossible")
        exit()
    if '_' in l:
        print("Game not finished")
        exit()


def segregate(l):
    row = [l[index:index + 3] for index in range(0, len(l), 3)]
    column = [l[index] + l[index + 3] + l[index + 6] for index in range(3)]
    cross = [l[0] + l[4] + l[8], l[2] + l[4] + l[6]]
    return row + column + cross


def reduce(seg_line):
    return [check for check in seg_line if len(set(check)) == 1]


def draw(outcome):
    if len(outcome) == 0:
        print("Draw")
        exit()


def win(outcome):
    if len(outcome) == 1:
        if set(list(outcome[0])) == set('X'):
            print("X wins")
            exit()
        elif set(list(outcome[0])) == set('O'):
            print("O wins")
            exit()


def impossible(outcome):
    if len(outcome) > 1:
        print("Impossible")
        exit()


def process_ttt(line):
    segregated_line = segregate(line)
    reduced_result = reduce(segregated_line)
    win(reduced_result)
    # impossible(reduced_result)
    # game_not_finished(line)
    if len(line.replace('_', '').replace(' ', '')) == 9:
        draw(reduced_result)


def handle_input(line):
    # print_ttt(line)
    process_ttt(line)


def handle_coordinates(row, column):
    if not (row.isnumeric() and column.isnumeric()):
        print("You should enter numbers!")
        return False
    row = int(row)
    column = int(column)
    if row not in [1, 2, 3] or column not in [1, 2, 3]:
        print("Coordinates should be from 1 to 3!")
        return False
    row = 4 - int(row)
    column = int(column)
    ttt_index = (row - 1) * 3 + (column - 1)
    if ttt_list[ttt_index] not in [' ', '_']:
        print("This cell is occupied! Choose another one!")
        return False
    return True


def update_ttt_list(ttt_list, row, column, turn):
    row = 4-int(row)
    column = int(column)
    ttt_index = (row - 1) * 3 + (column - 1)
    if ttt_list[ttt_index] in [' ', '_']:
        ttt_list = ttt_list[:ttt_index]+turn+ttt_list[ttt_index+1:]
    return ttt_list


ttt_list = "_________"
print_ttt(ttt_list)
turn = 'X'
while True:
    proper = False
    while not proper:
        column, row = input("Enter the coordinates: ").split()
        proper = handle_coordinates(row, column)
        if proper:
            ttt_list = update_ttt_list(ttt_list, row, column, turn)
            if turn == 'X':
                turn = 'O'
            else:
                turn = 'X'
    print_ttt(ttt_list)
    handle_input(ttt_list)
