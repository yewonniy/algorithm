T = int(input())
score = 0
total_score = 0
score_list = list()

for i in range(0, T):
    result = list(input())
    for j in range(0, len(result)):
        if result[j] == 'O':
            for k in range(1, j+1):
                if result[j-k] == 'O':
                    score = score+1
                else:
                    break
            score = score+1
            total_score = total_score + score
            score = 0
    score_list.append(total_score)
    total_score = 0

for i in range(0, len(score_list)):
    print(score_list[i])
