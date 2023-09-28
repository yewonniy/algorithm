n = int(input())
array = list(map(int, input().split()))
# maxi = -1000
# memo = array
#
# for i in range(0, n):
#     if len(memo) > 0:
#         maxi = max(maxi, max(memo))
#     memo = []
#     for j in range(i+1, n):
#         if j == i+1:
#             memo.append(array[i]+array[j])
#         else:
#             memo.append(memo[-1]+array[j])
# print(maxi)

for i in range(1, n):
   array[i] = max(array[i], array[i-1] + array[i])

print(max(array))