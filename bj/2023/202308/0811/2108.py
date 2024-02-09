import sys
from collections import Counter

N = int(sys.stdin.readline())
num_list = []

for _ in range(N):
    num_list.append(int(sys.stdin.readline()))
num_list.sort()

cnt_num = Counter(num_list).most_common()
if len(cnt_num) > 1 and cnt_num[0][1] == cnt_num[1][1]:
    popular = cnt_num[1][0]
else:
    popular = cnt_num[0][0]

print(round(float(sum(num_list))/float(N)))
print(num_list[N//2])
print(popular)
print(num_list[N-1]-num_list[0])