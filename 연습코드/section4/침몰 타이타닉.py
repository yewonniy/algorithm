from collections import deque
n, m = map(int, input().split()) # 승객, 보트 무게
weights = list(map(int, input().split())) # 승객 몸무게 <= m
weights.sort(reverse=True)
passengers = deque(weights)

cnt = 0
while passengers:
    if len(passengers) > 1 and passengers[0] + passengers[-1] <= m:
        passengers.pop()
    passengers.popleft()
    cnt += 1
print(cnt)
