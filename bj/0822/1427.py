n = list(input())

for i in range(len(n)):
    n[i] = int(n[i])

n.sort(reverse=True)
for x in n:
    print(x, end='')