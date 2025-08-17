n = int(input())


def div_mod(x: int, res: str):
    div_ = x // 2
    mod = x % 2
    x = x // 2
    if div_ == 0:
        print(str(mod)+res)
        return
    res = str(mod) + res
    div_mod(x, res)


div_mod(n, "")