maximum = 0
output = ''
while True:
    string = input()
    if ' ' in string:
        cafe, number = string.split(' ')
    else:
        break
    number = int(number)
    if number > maximum:
        maximum = number
        output = cafe

print(output)
