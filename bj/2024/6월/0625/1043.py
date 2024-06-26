n, m = map(int, input().split())  # 사람 수, 파티수
arr = list(map(int, input().split())) # arr[1]부터 진실을 아는 사람
party = []
for _ in range(m):
    l = list(map(int, input().split()))
    party.append(l[1:])  # party

if arr[0] == 0:
    print(m)
# else:
#     # bfs? dfs?