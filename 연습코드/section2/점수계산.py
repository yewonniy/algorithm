n = int(input())
arr = list(map(int, input().split()))
score = [0] * n

for i in range(0, n):
    if arr[i] == 1:
        score[i] = score[i-1]+1

print(sum(score))