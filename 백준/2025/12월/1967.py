from collections import defaultdict
n = int(input())
arr = defaultdict(list)
key = set()
for _ in range(n-1):
    parent, child, weight = map(int, input().split())
    arr[parent].append((weight, child))
    key.add(parent)
maxi = 0


def dfs(c, node, internal):
    global maxi
    if not arr[node]:  # 리프노드까지 도착!
        # print(root,"->",node,"까지 거리=",c)
        for list_, cost in res:
            if len(set(internal) - set(list_)) == 1: # 경로는 루트만 겹쳐야 함.
                maxi = max(maxi, cost+c)
        res.append((internal[:], c))
    else:  # 아직 internal 노드
        for cost, next_node in arr[node]:
            internal.append(next_node)
            dfs(c+cost, next_node, internal)
            internal.pop()


for node in key:
    # print(node,"가 루트")
    res = []
    dfs(0, node, [node])
print(maxi)