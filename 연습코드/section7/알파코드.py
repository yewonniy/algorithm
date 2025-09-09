code = list(input()) # 1~26 chr(code + 64)하면 됨.
lim = len(code)
cnt = 0


def dfs(L, decode):
    global cnt
    if L == lim:
        cnt += 1
        for n in decode:
            print(chr(int(n)+64),end='')
        print()
        return
    target = code[L]
    if target != "0":
        decode.append(target)
        dfs(L+1, decode)
        if len(decode) > 0:
            decode.pop()
    if len(decode) > 0:
        last = decode.pop()
        if 0 < int(last + target) <= 26:
            decode.append(last + target)
            dfs(L+1, decode)
        else:
            decode.append(last)


dfs(1, list(code[0]))
print(cnt)