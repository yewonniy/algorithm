from collections import defaultdict
import sys
n = int(input())
num = [int(sys.stdin.readline()) for _ in range(n)]

print(round(sum(num)/n))

num.sort()
print(num[n//2])

dic = defaultdict(int)
for x in num:
    dic[x] += 1
maxi = max(dic.values())
res = []
for key in dic:
    if dic[key] == maxi:
        res.append(key)
res.sort()
if len(res) > 1:
    print(res[1])
else:
    print(res[0])
print(num[-1]-num[0])