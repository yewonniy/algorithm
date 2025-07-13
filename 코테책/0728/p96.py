n, m = map(int, input().split())

mini = 0
for i in range(n):
    min_current = (min(map(int, input().split())))
    if min_current > mini:
        mini = min_current

print(mini)