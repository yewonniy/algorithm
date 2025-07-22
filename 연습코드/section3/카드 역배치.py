card = [i for i in range(1, 21)]

for i in range(10):
    a, b = map(int, input().split())
    temp = card[a-1:b]
    k = 1
    for j in range(a-1,b):
        card[j] = temp[-k]
        k += 1
for i in card:
    print(i, end=' ')