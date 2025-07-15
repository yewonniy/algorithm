n = int(input())
array = list(map(int, input().split()))


def check(i:int) -> bool:
    if i == 1: return False
    if i == 2: return True
    for n in range(2, int(i**0.5)+2):
        if i % n == 0:
            # 소수 아님
            return False
    return True


cnt = 0
for i in array:
    if check(i):
        cnt +=1
print(cnt)