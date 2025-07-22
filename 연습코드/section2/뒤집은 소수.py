n = int(input())
arr = list(map(str, input().split()))


def reverse(x: str):
    res = list(x)
    ans = ''
    for i in range(-1, -(len(res) + 1), -1):
        ans += res[i]
    return int(ans)


def reverse2(x: str):  # ** 10으로 나눈 몫과 나머지로 뒤집는 방법! **
    res = 0
    l = len(x)-1
    n = int(x)
    for i in range(l+1):
        temp = n % 10
        res += temp * 10**l
        n = n//10
        l -= 1
    return res

def reverse3(x:str):
    res = int(x[::-1])
    return res


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
    num = reverse3(x)
    if is_prime(num):
        print(num, end=' ')

