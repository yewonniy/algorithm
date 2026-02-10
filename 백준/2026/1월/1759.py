l, c = map(int, input().split())
arr = list(input().split(' '))
arr.sort()
moum = ('a','e','i','o','u')
# 모음 1개, 자음 2개 이상 써서 l 길이의 암호


def backtracking(L, word, mo, ja, idx):
    if L == l:
        if mo >= 1 and ja >= 2:
            print(word)
        return
    for i in range(idx, c):
        alphabet = arr[i]
        if alphabet in moum:
            backtracking(L+1, word+alphabet, mo+1, ja, i+1)
        else:
            backtracking(L+1, word+alphabet, mo, ja+1, i+1)


backtracking(0, "", 0, 0, 0)