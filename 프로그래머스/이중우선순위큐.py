import heapq


def solution(operations):
    min_heap = []
    max_heap = []
    for operation in operations:
        op, n = operation.split()
        if op == "I":
            heapq.heappush(min_heap, int(n))
            heapq.heappush(max_heap, -int(n))
        elif op == "D" and len(max_heap) > 0:
            if n == "1":
                num = heapq.heappop(max_heap)
                min_heap.remove(-num)
            else:
                num = heapq.heappop(min_heap)
                max_heap.remove(-num)
    if len(min_heap) == 0:
        return [0,0]
    return [max(min_heap), min(min_heap)]