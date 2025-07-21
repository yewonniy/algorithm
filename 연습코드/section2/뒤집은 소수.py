n = int(input())
arr = list(map(str, input().split()))


def reverse(x: str):
    res = list(x)
    ans = ''
    for i in range(-1, -(len(res) + 1), -1):
        ans += res[i]
    return int(ans)


def is_prime(x: int):
    if x == 2 or x == 3:
        return True
    if x == 1:
        return False
    for i in range(2, int((x**0.5)+3)):
        if x % i == 0:
            return False
    return True


for x in arr:
    num = reverse(x)
    if is_prime(num):
        print(num, end=' ')

