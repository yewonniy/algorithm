def prime(num):
    if num == 1:
        return False
    if num == 2:
        return True
    for i in range(2, int(num ** (1 / 2)) + 2):
        if num % i == 0:
            return False
    return True


def is_prime(arr, idx):
    if arr[idx] == '0':
        return [idx + 1, False]
    num = ''
    for i in range(idx, len(arr)):
        nxt = i
        if arr[i] == '0':
            nxt -= 1
            break
        num += arr[i]

    if prime(int(num)):
        return [nxt + 1, True]
    return [nxt + 1, False]


def solution(n, k):
    # 1. n을 k진수로 바꾼다.
    a = ''
    while n != 0:
        a += str(n % k)
        n = n // k
    newN = list(a)[::-1]

    ans = 0
    # 2. k진수가 된 newN에서 소수를 찾는다.
    idx = 0
    while idx < len(newN):
        new_idx, isPrime = is_prime(newN, idx)
        idx = new_idx
        if isPrime:
            ans += 1
    return ans