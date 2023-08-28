a, b, c = map(int, input().split())
memo = [0] * (b+1)
memo[0] = 1
memo[1] = a


def mul(x, y):
    cnt = 1
    result = a
    if y % 2 == 0:
        while cnt < y:
            if y <= 2*cnt:
                result = result * memo[y-cnt]
                return result
            else:
                result *= result
                cnt *= 2
                memo[cnt] = result
    else:
        memo[2] = x*x
        memo[3] = x**3
        result = memo[3]
        cnt = 3
        while cnt < y:
            if y <= 2*cnt:
                if memo[y-cnt] != 0:
                    result = result * memo[y-cnt]
                else:
                    result = result * (x**(y-cnt))
                return result
            else:
                result *= result
                cnt *= 2
                memo[cnt] = result


if b > 3:
    ans = mul(a, b)
else:
    ans = a**b

print(ans % c)