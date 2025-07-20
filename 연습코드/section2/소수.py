n = int(input())

cnt = 0
# for i in range(2, n+1):
#     for j in range(2, int(i**0.5 + 2)):
#         if i != j and i % j == 0:  # 소수 아님
#             break
#     else:  # 소수임
#         cnt += 1
# print(cnt)

## 생각의 전환!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
ch = [0] * (n+1)
for i in range(2, n+1):
    if ch[i] == 0:
        cnt += 1
        for j in range(i, n+1, i):
            ch[j] = 1

print(cnt)