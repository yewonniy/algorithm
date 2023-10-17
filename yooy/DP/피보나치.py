memo = [0, 1, 1]


def fibo(n):
    if len(memo)-1 >= n:
        return memo[n]
    else:
        while len(memo)-1 < n:
            memo.append(memo[-1] + memo[-2])
            print(memo)
            if len(memo)-1 == n:
                return memo[n]


print(fibo(8))
print(fibo(9))