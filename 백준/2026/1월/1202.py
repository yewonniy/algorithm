import sys, heapq
input = sys.stdin.readline

n, k = map(int, input().split())  # 보석 수, 가방 수
arr = [list(map(int, input().split())) for _ in range(n)]  # n개의 보석 [[무게, 가치], [무게, 가치] ... [무게, 가치]]
bags = [int(input()) for _ in range(k)]  # 가방에 담을 수 있는 무게 (딱 1개의 보석만 담을 수 있음)
bags.sort()  # 가벼운 순서대로 정렬
arr.sort(key=lambda x: x[0])  # 가벼운 순서대로 정렬

# 내가 그동안 한 방식 : 어 나 i번째로 가치 큰 보석인데! 난 어느 가방에 들어갈 수 있으려나~?
# 지금부터는 : 어 나 i번째 가방인데, 어떤 보석을 넣는 게 제일 좋을까?
res = 0
q = []
idx = 0
for bag in bags:
    # 지금 bag 용량 보다 가벼운 보석들 다 heap에 들어가!
    for i in range(idx, n):
        w, v = arr[i]
        if w <= bag:
            heapq.heappush(q, (-v, w))
        else:
            idx = i
            break
    else:
        idx = n
    if q:
        v, w = heapq.heappop(q)
        res += (-v)
print(res)

