a = list(input())
b = list(input())
memo = [[0] * (len(a)+1) for _ in range(len(b)+1)]

for i in range(1, len(b)+1):
    for j in range(1, len(a)+1):
        if b[i-1] == a[j-1]:
            memo[i][j] = memo[i-1][j-1] + 1
        else:
            memo[i][j] = max(memo[i-1][j], memo[i][j-1])
res = memo[len(b)][len(a)]
print(res)
if res > 0:
    word = []
    x, y = len(b), len(a)
    while x > 0 and y > 0:
        if b[x-1] == a[y-1]:
            word.append(b[x-1])
            x -= 1
            y -= 1
        else:
            if memo[x-1][y] > memo[x][y-1]:
                x -= 1
            else:
                y -= 1
    print(''.join(word[::-1]))