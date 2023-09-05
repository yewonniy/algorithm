import sys

n, m = map(int, input().split())

dict_ = {}
for i in range(n):
    list_ = list(sys.stdin.readline().split())
    dict_[list_[0]] = list_[1]

find = []
for i in range(m):
    k = sys.stdin.readline().rstrip()
    find.append(dict_[k])

for x in find:
    print(x)
