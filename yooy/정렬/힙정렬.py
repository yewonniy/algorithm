import heapq # 파이썬 heap -> 최소 힙이므로 루트([0])는 무조건 최소인 게 보장됨
num = list(map(int, input().split()))

heap_list = []
result = []

for x in num: # 힙에 데이터 n개 삽입
    heapq.heappush(heap_list, x)

for i in range(len(heap_list)): # heap이 빌 때까지 데이터를 다 제거 (루트 제거)
    x = heapq.heappop(heap_list)
    result.append(x)

