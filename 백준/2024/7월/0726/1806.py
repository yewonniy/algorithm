n, s = map(int, input().split())  # 수열 길이 (100,000) , 부분 수열의 합이 >= s 중 가장 길이가 짧은 수열
num = list(map(int, input().split()))
dy = [0] * n

if sum(num) < s:
    print(0)
else:
    res = n
    for i in range(n):
        for j in range(i, n):
            if i == 0:
                if j == 0:
                    dy[j] = num[j]
                else:
                    dy[j] = dy[j-1] + num[j]
            else:
                dy[j] = dy[j] - num[i-1]
            if dy[j] >= s:
                res = min(res, j-i+1)
    print(res)