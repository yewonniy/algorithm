str1 = list(input())
str2 = list(input())


def dfs(arr, check, ch):
    for i in range(len(arr)):
        if arr[i] == str2[0]:  # 폭발 문자열의 첫 글자를 발견했다!
            start = i
            for j in range(1, len(str2)):
                if arr[start + j] != str2[j]:  # 폭발 문자열이 아니었네~
                    break
                if arr[start + j] == str2[j] and j == len(str2)-1:  # 폭발 문자열 있음!
                    last = start + j
                    for idx in range(start, last+1):
                        check[idx] = False
                    i = last
                    ch = True  # True면 폭발물을 제거했단 뜻, False 면 더이상 제거할 게 없다는 뜻
    if check.count(True) == 0:
        print("FRULA")
        return
    if ch:
        new = []
        for i in range(len(arr)):
            if check[i]:
                new.append(arr[i])
        dfs(new, [True] * len(new), False)
    else:
        for x in arr:
            print(x, end='')
        return


dfs(str1, [True] * len(str1), False)