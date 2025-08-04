n = int(input())
arr = list(map(int, input().split())) # 역수열
res = [0] * n
res[arr[0]] = 1

flag = 0
for i in range(1, n):
    cnt = 0
    if arr[i] == 0 and flag == 0:
        flag = 1
        res[0] = i+1
    else:
        for j in range(n):
            if res[j] == 0:
                cnt += 1
            if cnt == arr[i]:
                for k in range(j+1, n):
                    if res[k] == 0:
                        res[k] = i+1
                        break
                break

m = ''
for x in res:
    m += (str(x)+' ')
print(m)
print(m.strip()==input().strip())