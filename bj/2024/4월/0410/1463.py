# 정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.
# X가 3으로 나누어 떨어지면, 3으로 나눈다.
# X가 2로 나누어 떨어지면, 2로 나눈다.
# 1을 뺀다.
# 정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.

n = int(input())
count_list = [100000000]


def make_one(x, count):
    if x % 3 == 0:
        make_one(x // 3, count + 1)
    if x % 2 == 0:
        make_one(x // 2, count + 1)
    if x > 1:
        make_one(x - 1, count + 1)
    if x <= 1:
        result = min(count_list)
        if count < result:
            count_list.append(count)
        x = n
        count = 0


make_one(n, 0)
print(min(count_list))
