# 정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.
# X가 3으로 나누어 떨어지면, 3으로 나눈다.
# X가 2로 나누어 떨어지면, 2로 나눈다.
# 1을 뺀다.
# 정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.
# 1 <= n <= 10**6

n = int(input())

memo = [99999999] * (10**6 + 1)
memo[1] = 0
memo[2] = 1

for i in range(3, n+1):
    two = 999999
    three = 999999
    one = memo[i-1] + 1
    if i % 2 == 0:
        two = memo[i//2] + 1
    if i % 3 == 0:
        three = memo[i//3] + 1
    memo[i] = min(one, two, three)


# result
print(memo[:n+1])
print(memo[n])