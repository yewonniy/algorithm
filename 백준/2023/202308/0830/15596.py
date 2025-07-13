n = int(input())


def sum_(k):
    result = 0
    for i in range(1, k+1):
        result += i
    return result


res = sum_(n)
print(res)