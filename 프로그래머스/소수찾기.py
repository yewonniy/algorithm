from itertools import permutations

def is_prime(num):
    if num == 0 or num == 1: return False
    if num == 2: return True
    for i in range(2, int(num**0.5+2)):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    res = set()
    for i in range(1, len(numbers)+1):
        t = list(permutations(numbers, i))
        for j in range(len(t)):
            n = ""
            for k in range(len(t[j])):
                n += t[j][k]
            if is_prime(int(n)):
                res.add(int(n))
    print(res)
    return len(res)