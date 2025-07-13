K, N = input().split()
K = int(K)
N = int(N)

len_list = list()

for i in range(0, K):
    length = int(input())
    len_list.append(length)

max_len = max(len_list) #얠 구해야 함
min_len = min(len_list)

cnt_max = 0
cnt_min = 0
for i in range(0, K):
    cnt_max += (len_list[i])//max_len
    cnt_min += (len_list[i])//min_len
if (cnt_min <= N) and (cnt_max < N):
    max_len = min_len

for j in range(0, max_len):
    cnt_max = 0
    for i in range(0, K):
        cnt_max += (len_list[i])//max_len
    if cnt_max >= N:
        print(max_len)
        break
    max_len = max_len-1
