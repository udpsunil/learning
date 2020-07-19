# read sums.txt
with open('sums.txt') as read_file:
    for line in read_file:
        print(sum(int(x) for x in line.split(' ')))
