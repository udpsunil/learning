# put your python code here
duration = int(input())
daily_food_cost = int(input())
flight_cost = int(input())
hotel_cost = int(input())
total_cost = (daily_food_cost * duration) + 2 * flight_cost + (hotel_cost * (duration - 1))
print(total_cost)
