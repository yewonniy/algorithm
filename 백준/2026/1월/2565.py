import sys
input = sys.stdin.readline

n = int(input())  # n = 100 (n^2가능)
arr = [list(map(int, input().split())) for _ in range(n)]

arr.sort(key=lambda x: x[0])
memo = [1] * n # i번째 전깃줄을 "마지막으로 선택했을 때"의 최대길이

for i in range(n):
    for j in range(i):
        # 1. 내 앞에 있는 애들을 다 훑어봄
        # 2. arr[j]를 내 앞에 붙일 수 있으면
        if arr[i][1] > arr[j][1]:
            memo[i] = max(memo[i], memo[j]+1)