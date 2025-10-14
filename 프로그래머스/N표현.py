def solution(N, number):
    answer = 0
    dp = [set() for _ in range(9)] # 9부턴 return -1
    for k in range(1,9):
        dp[k].add(int(str(N)*k))
        for i in range(1, k):
            arr1 = dp[i]
            arr2 = dp[k-i]
            for x in arr1:
                for y in arr2:
                    dp[k].add(x+y)
                    dp[k].add(x-y)
                    dp[k].add(x*y)
                    if y != 0:
                        dp[k].add(x/y)
        if number in dp[k]:
            return k
    return -1