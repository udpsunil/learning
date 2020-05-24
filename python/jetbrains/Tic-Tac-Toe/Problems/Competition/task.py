check = all([True, True, 1, 1, True])

status = 'winner' if check else 'loser'
winning_sum = 100 if status == 'winner' else 10
