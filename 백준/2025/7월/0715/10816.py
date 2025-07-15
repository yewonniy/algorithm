# 해시 자료구조 (dictionary) 공부

n = int(input())
card = list(map(int, input().split()))
m = int(input())
how_many = list(map(int, input().split()))

dict = {}
for i in range(n):
    if card[i] in dict:
        # 해당 value 값을 +1
        dict[card[i]] += 1
    else:
        # 새롭게 key, value 쌍 추가
        dict[card[i]] = 1

for i in range(m):
    if how_many[i] in dict:
        print(dict[how_many[i]], end=' ')
    else:
        print(0, end=' ')