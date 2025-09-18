answer = 100000
def dfs(info, n, m, a_sum, b_sum, visited, l):
    global answer
    if l == len(info) and a_sum < n and b_sum < m:
        answer = min(answer, a_sum)
        return
    if l == len(info) or a_sum >= n or b_sum >= m:
        return
    if (a_sum, b_sum, l) in visited:
        return
    visited.add((a_sum, b_sum, l))
    dfs(info, n, m, a_sum + info[l][0], b_sum, visited, l+1)
    dfs(info, n, m, a_sum, b_sum + info[l][1], visited, l+1)


def solution(info, n, m):
    global answer
    dfs(info, n, m, 0, 0, set(), 0)
    if answer == 100000:
        return -1
    return answer