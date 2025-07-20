from itertools import combinations
n, k = map(int, input().split())
card = list(map(int, input().split()))

res = set()
for mini_arr in combinations(card, 3):
    res.add(sum(mini_arr))
res = list(res)
res.sort(reverse=True)
print(res[k-1])