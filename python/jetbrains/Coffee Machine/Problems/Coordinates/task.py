number1 = float(input())
number2 = float(input())

if number1 > 0 and number2 > 0:
    print('I')
elif number1 > 0 and number2 < 0:
    print('IV')
elif number1 < 0 and number2 > 0:
    print('II')
elif number1 < 0 and number2 < 0:
    print('III')
else:
    print('origin')
