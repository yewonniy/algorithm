n = int(input())  # 전체 사람 수
a, b = map(int, input().split())  # 촌수 계산 타겟
m = int(input())  # 부모 자식 간의 관계의 개수

graph = [[] for _ in range(n+1)]
for _ in range(m):
    parent, child = map(int, input().split())
    graph[parent].append(child)


def dfs(index, cnt):
    global a_cnt, b_cnt
    if index == a:
        a_cnt = cnt
    elif index == b:
        b_cnt = cnt
    if len(graph[index]) > 0:
        for num in graph[index]:
            dfs(num, cnt+1)


res = float('inf')
for i in range(1, n+1):
    a_cnt, b_cnt = -1, -1
    dfs(i, 0)
    if a_cnt != -1 and b_cnt != -1:
        res = min(a_cnt + b_cnt, res)

if res == float('inf'):
    print(-1)
else:
    print(res)