n = int(input())
score = list(map(int, input().split()))
average = int((sum(score) / n) + 0.5)

lower = []
higher = []
for i in range(n):
    if score[i] >= average:
        higher.append([i, score[i]-average])
    else:
        lower.append([i, average-score[i]])
higher.sort(key=lambda x: (x[1], x[0]))
lower.sort(key=lambda x: (x[1], x[0]))

if higher[0][1] <= lower[0][1]:  # 더 작은 애 출력, 같다면 higher 쪽 출력
    print(average, higher[0][0]+1)
else:
    print(average, lower[0][0]+1)