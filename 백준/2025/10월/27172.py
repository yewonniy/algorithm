N = int(input())
card = list(map(int, input().split()))
index_map = {v : i for i, v in enumerate(card)}
card.sort()
res = [0] * N

for i in range(N):
    v = card[i]
    idx = index_map[v]
    multiple = 2 * v
    while multiple <= card[-1]:
        if multiple in index_map:
            res[index_map[multiple]] -= 1
            res[idx] += 1
        multiple += v

print(' '.join(list(map(str, res))))