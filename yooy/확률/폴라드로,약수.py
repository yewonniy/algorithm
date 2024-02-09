def GCD(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a >= b:
        return GCD(a % b, b)
    if a <= b:
        return GCD(a, b % a)


def g(x):
    return x**2 + 1


def PR(n, x1, x2):
    while True:
        x1 = g(x1) % n
        x2 = g(g(x2)) % n
        if x1 == x2:
            return "FAIL"
        if GCD(abs(x1-x2), n) > 1:
            return GCD(abs(x1-x2), n)


PR(15, 0, 0)