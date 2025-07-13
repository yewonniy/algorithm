n = int(input())

fact = [0]*1000


def factorial(num):
    result = 1
    for x in range(num, 0, -1):
        result = result * x
    fact[num] = result
    return fact[num]


count = 1
for i in range(n//2 + 1, 0, -1):
    if 2*i < n:
        j = n - 2*i
        count += (factorial(i+j))//((factorial(i))*(factorial(j)))
    elif 2*i == n:
        count += 1

print(count % 10007)