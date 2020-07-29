# Do not re-calculate already calculated information. Store them in a list / data structure. Memoization.
# Cache the result of computation -> time - memory trade of

# Climbing stairs problem
# In how many distinct ways can you climb to the top?
# Constraints - 1 or 2 steps at a time

# Define an objective function -> function that need to be minimize(cost) or maximize(profit)
# So, this problem is minimization problem

# 1. Define Objective Function: f(i) is number of distinct ways to reach the ith stair
# 2. Identify the base cases: Break down the problem into simpler sub-problems
# -- Solve the problem for basic cases for which computing is not required.
# -- When we only have 2 stairs?
# ---- There are only 2 stair -> (1, 1) and (2) are the only 2 ways f(2) => 2
# ---- There is only 1 stair -> (1) is the only 1 way f(1) => 1
# ---- Smallest sub problem is when we don't have stair at f(0) => 1 : Do nothing also counts as a way to top.
# -- By looking at the problem from top to bottom, combinatorics --> rule of sum
# -- f(n) = f(n-1) + f(n-2) --> set theory union operation of 2 disjoint sets
# 3. Recurrence relation
# 4. Order of computation
# 5. Location of the answer

def climbing_stairs(n):
    solution = [1, 1]
    for i in range(2, n+1):
        solution.append(solution[i-1]+solution[i-2])
    return solution[n]



