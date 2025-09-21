answer = -1
res = -2


def dfs(word, alphabet, L, now):
    global answer, res
    answer += 1
    if res != -2:
        return
    if now == word:
        res = answer
        return res
    if L == 5:
        return
    for i in range(5):
        dfs(word, alphabet, L + 1, now + alphabet[i])


def solution(word):
    global answer, res
    dfs(word, ["A", "E", "I", "O", "U"], 0, "")
    return res