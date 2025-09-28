n, t = map(int, input().split()) # t 분 후 그룹 수
p = []
s = []
for i in range(n):
    a, b = map(int, input().split())
    p.append(a)
    s.append(b)
p = p[::-1]
s = s[::-1]

for i in range(n-1):
    if p[i] + s[i] * t <= p[i+1] + s[i+1] * t: # 동기화
        p[i+1] = p[i]
        s[i+1] = s[i]

res = set()
for x in p:
    res.add(x)
print(len(res))
