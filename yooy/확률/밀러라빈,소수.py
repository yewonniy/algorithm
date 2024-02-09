def mr_prime(n, a):
    s = 0
    d = n - 1
    while True:
        if d % 2 == 0:
            d = d//2
            s += 1
        else:
            break
    if (a ** d) % n == 1:
        return "Maybe Prime"
    for i in range(0, s):
        if (a ** ((2**i)*d)) % n == -1:
            return "Maybe Prime"
    return "Definitely not prime"
