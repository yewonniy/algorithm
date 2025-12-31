# R : 뒤집기, D : 첫번째 수 버리기
import sys
from collections import deque
t = int(input())
for _ in range(t):
    p = list(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())
    reverse = False
    if n == 0:
        sys.stdin.readline()
        nums = list()
    else:
        nums = deque(list(map(int, sys.stdin.readline().rstrip().lstrip('[').rstrip(']').split(','))))
    for x in p:
        if x == 'R':
            if reverse:
                reverse = False
            else:
                reverse = True
        else:
            if len(nums) > 0:
                if reverse:
                    nums.pop()
                else:
                    nums.popleft()
            else:
                print('error')
                break
    else:
        if reverse:
            nums.reverse()
        print('['+','.join(list(map(str, nums))) +']')

