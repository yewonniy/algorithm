n, k = map(int, input().split())
l = len(str(n)) - k # 만들어 지는 자릿수

arr = list(str(n))
maxi = int(arr[0])
index = 0
for i in range(k+1):
    if int(arr[i]) > maxi:
        index = i
        maxi = int(arr[i]) # maxi가 수의 맨 첫자리가 됨
        k -= 1

for i in range(index):
    print(arr, k)
    arr.pop(0)
k+=1
m = k


def popping(array, k):
    for i in range(len(arr)-k):
        cnt = 0
        index = i
        for j in range(k):
            if int(array[i+j]) < int(array[i+j+1]):
                cnt = 1
                index = i+j
        if cnt == 1:
            array.pop(index)
            return
    array.pop()


for p in range(m):
    popping(arr, k)
    k-=1
res = ''
for x in arr:
    res+=x
print(int(res)==int(input()))