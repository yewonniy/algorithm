n = int(input())
mid = int(n//2)
apples = 0
for i in range(n):
    trees = list(map(int, input().split()))
    if i <= mid:
        apples += sum(trees[mid-i: mid+i+1])
    else:
        k = n-i-1
        apples += sum(trees[mid-k:mid+k+1])
print(apples)