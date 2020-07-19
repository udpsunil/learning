# read sample.txt and print the number of lines
with open('sample.txt') as read_file:
    print(len(read_file.readlines()))
