n, m = map(int, input().split())
m_arr = list(map(int, input().split())) # 이걸 합쳐서  >= m 이어야 함
c_arr = list(map(int, input().split())) # 그중에 sum c가 min인 것!
mini = sum(c_arr) + 1


def dfs(level, tot, c_sum):
    global mini
    if tot >= m:
        mini = min(mini, c_sum)
        return
    if level >= n:
        return
    dfs(level+1, tot + m_arr[level], c_sum + c_arr[level])
    dfs(level+1, tot, c_sum)


dfs(0, 0, 0)
print(mini)