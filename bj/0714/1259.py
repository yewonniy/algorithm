while (True):
    n = int(input())
    k = 0
    pel = 0
    if n == 0:
        break
    n_list = list((str(n)))
    p = len(n_list)
    if len(n_list) % 2 == 1:
        while len(n_list) > p//2+1:
            former = n_list[k]
            latter = n_list.pop()
            k += 1
            if former == latter:
                pel += 1
            else:
                print("no")
                break
        if pel == p//2:
            print("yes")
    else:
        while len(n_list) > p//2:
            former = n_list[k]
            latter = n_list.pop()
            k += 1
            if former == latter:
                pel += 1
            else:
                print("no")
                break
        if pel == p//2:
            print("yes")
