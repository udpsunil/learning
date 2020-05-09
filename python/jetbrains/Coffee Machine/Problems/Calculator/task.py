# put your python code here
first_num = float(input())
second_num = float(input())
operation = input()
output = None

if operation == '+':
    output = first_num + second_num
elif operation == '-':
    output = first_num - second_num
elif operation == '/':
    if second_num == 0:
        output = 'Division by 0!'
    else:
        output = first_num / second_num
elif operation == '*':
    output = first_num * second_num
elif operation == 'mod':
    if second_num == 0:
        output = 'Division by 0!'
    else:
        output = first_num % second_num
elif operation == 'pow':
    output = first_num ** second_num
elif operation == 'div':
    if second_num == 0:
        output = 'Division by 0!'
    else:
        output = first_num // second_num
print(output)
