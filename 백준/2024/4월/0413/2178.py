n, m = map(int, input().split())
miro = []
for i in range(n):
    miro.append(list(input()))

# (0, 0) -> (n-1, m-1)
print(miro)
# for x in range(n):
#     for y in range(m):