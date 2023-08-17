n = int(input())

fact = [0]*1000


def factorial(num):
    if num == 1:
        return 1
    if fact[num] != 0:
        return fact[num]
    fact[num] = num*factorial(num-1)
    return fact[num]


cnt = 1
for i in range(n//2 + 1, 0, -1):
    if 2*i < n:
        j = n - 2*i
        cnt += (factorial(i+j))//((factorial(i))*(factorial(j)))
    elif 2*i == n:
        cnt += 1

print(cnt % 10007)