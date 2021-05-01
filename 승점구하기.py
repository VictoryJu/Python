def foo(games):
    score = games
    rank = 0
    for i in range(len(score)):
        if score[i][0] > score[i][2]:
            rank += 3
        elif score[i][0] == score[i][2]:
            rank += 1
        else:
            rank += 0

    return rank

score = ["3:1","2:2","1:3","3:1"]
result = foo(score)
print(result)
