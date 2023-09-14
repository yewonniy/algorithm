n = int(input())

num = []
for x in range(n):
    if n - x <= 9*len(str(n)):
        k = x
        p = x
        for j in range(len(str(x))):
            p += k % 10
            k = k // 10
        if p == n:
            print(x)
            break
