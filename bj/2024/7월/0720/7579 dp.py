n, m = map(int, input().split())
m_arr = list(map(int, input().split())) # 이걸 합쳐서  >= m 이어야 함
c_arr = list(map(int, input().split())) # 그중에 sum c가 min인 것!

dy = [[-1] * (m+1) for _ in range(n)]

for i in range(n):
    # 본인까진 min(dy[i-1][j], c_arr[i])
    # 본인 이후부턴 min(dy[i-1][j-m_arr[i]] + c_arr[i], -> 근데 dy[i-1][j-m_arr[i]]가 -1이 아닌 경우에만! -1이 되면 멈추기
    for j in range(m + 1):
        if i == 0 and j <= m_arr[i]:
            dy[i][j] = c_arr[i]
        elif i > 0:
            if j <= m_arr[i]:
                dy[i][j] = min(dy[i-1][j], c_arr[i])
            else:
                if dy[i-1][j-m_arr[i]] == -1:
                    break
                dy[i][j] = dy[i-1][j-m_arr[i]] + c_arr[i]
res = sum(c_arr)
for x in dy:
    if -1 < x[60] < res:
        res = x[60]
print(res)
