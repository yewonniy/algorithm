import heapq
def solution(scoville, K):
    heap = []
    answer = 0
    for n in scoville:
        heapq.heappush(heap, n)
    while True:
        if len(heap) == 0:
            return -1
        if len(heap) == 1:
            if heap[0] > K:
                return answer
            return -1
        a = heapq.heappop(heap)
        if a >= K:
            break
        b = heapq.heappop(heap)
        heapq.heappush(heap, a+(b*2))
        answer += 1
    return answer