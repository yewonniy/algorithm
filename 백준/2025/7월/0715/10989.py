# 어떤 걸 기준으로 리스트를 구성하는 게 메모리를 아낄 수 있을지 잘 생각하기

import sys

n = int(input())
array = [0 for _ in range(10001)]
for i in range(n):
    array[int(sys.stdin.readline().strip())] += 1

for i in range(1, 10001):
    for j in range(array[i]):
        print(i)
