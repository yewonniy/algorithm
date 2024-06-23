def solution(words):
    n = len(words)
    k = len(words[0])

    for i in range(n):
        candidate = words[i]
        valid = True
        for j in range(n):
            if i == j:
                continue
            diffs = 0
            for x in range(k):
                if candidate[x] != words[j][x]:
                    diffs += 1
                if diffs > 1:
                    valid = False
                    break
            if not valid:
                break
        if valid:
            return candidate
    return ""


# 테스트 예제
print(solution(list(input().split())))