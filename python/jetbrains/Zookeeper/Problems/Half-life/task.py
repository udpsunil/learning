amount_atoms = int(input())
quantity = int(input())
half_life_days = 0
while amount_atoms > quantity:
    amount_atoms /= 2
    half_life_days += 12

print(half_life_days)
