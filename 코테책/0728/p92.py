N, M, K = map(int, input().split())

num_list = list(map(int, input().split()))

new_list = sorted(num_list)
sum = 0
i=0

if new_list[N-1] > new_list[N-2]:
    while i < M:
        for j in range(K):
            sum += new_list[N-1]
            i += 1
        sum += new_list[N-2]
        i+=1
else:
    for i in range(M):
        sum += new_list[N-1]

print(sum)