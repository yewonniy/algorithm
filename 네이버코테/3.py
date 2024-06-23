def solution(words):
    k = len(words[0])  # 각 str의 길이
    n = len(words)  # str의 총 개수
    res = [""] * k
    for i in range(n):
        word1 = words[i]
        for j in range(i+1, n):
            word2 = words[j]
            diff_cnt = 0
            for idx in range(k):
                if word1 == word2:
                    continue
                if word1[idx] == word2[idx]:
                    if res[idx] == "":
                        res[idx] = word1[idx]
                else:
                    diff_cnt += 1
                if diff_cnt > 2:  # 두 string 사이에 다른 char가 2개 초과면 정답이 나올 수 없다.
                    return ""
    for i in range(n):
        if res.count("") <= 0:
            break
        idx = res.index("")
        target = words[i]
        diff = 0
        for j in range(k):
            if target[j] != res[j]:
                diff += 1
            if diff > 1:
                res[idx] = target[idx]
    result = ""
    for x in res:
        if x == "":
            x = "a"
        result += x
    return result


print(solution(list(input().split())))