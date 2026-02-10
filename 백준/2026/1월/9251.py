first = list(input()) # 최대 1,000
second = list(input())
# dp 테이블을 2차원으로 써야된대
h, w = len(second), len(first)
memo = [[0] * (w+1) for _ in range(h+1)] # 패딩!!

for i in range(1, h+1):
    for j in range(1, w+1):
        if first[j-1] == second[i-1]:
            memo[i][j] = memo[i-1][j-1] + 1
        else:
            memo[i][j] = max(memo[i-1][j], memo[i][j-1])
print(memo[h][w])
