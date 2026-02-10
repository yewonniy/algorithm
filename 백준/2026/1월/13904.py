import sys, heapq
input = sys.stdin.readline
n = int(input())
arr = []
max_date = 0
for _ in range(n):  # [[남은 일수, 가치], ...]
    d, v = map(int, input().split())
    max_date = max(d, max_date)
    arr.append([d, v])
arr.sort(key=lambda x: -x[0])

# heap에 뭘 저장해? : date 날에 제출할 수 있는 모든 과제 중 가치가 젤 큰 것
idx = 0
res = 0
q = []
for date in range(max_date, 0, -1):
    for i in range(idx, n):
        if arr[i][0] >= date:
            heapq.heappush(q, (-arr[i][1], arr[i][0]))
        else:
            idx = i
            break
    else:
        idx = n
    if q:
        v, w = heapq.heappop(q)
        res += -v
print(res)