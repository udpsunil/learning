num_of_inputs = int(input())
for _ in range(num_of_inputs):
    number = int(input())
    if number ** 2 % 7 == 0:
        print(number**2)
