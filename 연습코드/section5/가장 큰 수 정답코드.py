n, k = input().split()
arr = list(map(int, n))
k = int(k)

### 내 앞에 나보다 작은 수가 있으면 안된다! (내림차순)
stack = [arr[0]]
for i in range(1, len(arr)):
    for j in range(len(stack)-1, -1, -1):
        if stack[j] < arr[i] and k > 0:
            stack.pop()
            k -= 1
    stack.append(arr[i])

# 아직 k가 남아있으면, 그만큼 맨 뒤에 놈들을 pop한다.
for i in range(k):
    stack.pop()
print(stack)