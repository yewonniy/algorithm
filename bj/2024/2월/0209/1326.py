from collections import deque

n = int(input())
bridge = [0] + list((map(int, input().split())))
a, b = map(int, input().split())

result = []
present = []


def pongdang(count, start, end, present):
    queue = deque([start])
    i = 1
    while start + bridge[start] * i <= end:
        now_node = start + bridge[start] * i
        present.append(now_node)
        i += 1
        if now_node == end:



pongdang(0, a, b, present)
# 7
# 2 2 1 1 1 3 2
# 1 6