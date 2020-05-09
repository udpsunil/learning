score = int(input())
max_score = int(input())
percentage = 100 * score / max_score
if 90.0 <= percentage <= 100.0:
    print("A")
elif 80.0 <= percentage <= 90.0:
    print("B")
elif 70.0 <= percentage <= 80.0:
    print("C")
elif 60.0 <= percentage <= 70.0:
    print("D")
else:
    print("F")
