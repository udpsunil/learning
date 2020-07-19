# Problem: Find sum of the first N numbers using dynamic programming
# Objective: f(i) is the sum of the first i elements
# Recurrence relation: f(i) = f(i-1) + i


def n_sum(n):
    dp = [0]
    for i in range(1,n+1):        
        dp.append(dp[i-1]+i)
    return dp[n]


assert n_sum(0) == 0
assert n_sum(1) == 1
assert n_sum(5) == 15
assert n_sum(10) == 55