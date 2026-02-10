import sys
input = sys.stdin.readline
n, m = map(int, input().split()) # 0 ~ n까지
parents = [i for i in range(n+1)]


def find_parent(a):
    while parents[a] != a:
        parents[a] = parents[parents[a]]
        a = parents[a]
    return parents[a]


def union(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a != b:
        parents[a] = b
    return b


def same_set(a,b):
    if find_parent(a) == find_parent(b):
        return True
    return False


for _ in range(m):
    op, a, b = map(int, input().split())
    if op == 0:
        union(a, b)
    elif same_set(a,b):
        print("YES")
    else:
        print("NO")

