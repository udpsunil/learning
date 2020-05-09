# put your python code here
number1 = int(input())
number2 = int(input())

sum = 0
count = 0

for number in range(number1, number2+1):
    if number % 3 == 0:
        sum += number
        count += 1

print(sum / count)
