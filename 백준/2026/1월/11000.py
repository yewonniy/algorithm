import sys, heapq

input = sys.stdin.readline

n = int(input())  # 20만
arr = [list(map(int, input().split())) for _ in range(n)]  # [[시작, 끝], [시작, 끝] ... [시작, 끝]]
arr.sort(key=lambda x: x[0])  # 수업을 '시작하는 시간이 빠른 순'으로 정렬
# 모든 수업을 하는데 필요한 강의실의 수 (최소)
# heap 의 용도 = 현재 열려있는 강의실들에서 진행 중인 강의가 몇시에 끝나는지. 그 숫자가 저장됨.
q = []
heapq.heappush(q, (arr[0][1]))
for i in range(1, n):
    start, end = arr[i]
    if start >= q[0]:
        heapq.heappop(q)
        heapq.heappush(q, end)
    else:  # 새 강의실 열어야 함
        heapq.heappush(q, end)
print(len(q))