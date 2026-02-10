k = int(input())
arr = list(input().split(' '))
maxi = -float("inf")
mini = float("inf")


def backtracking(idx):
    global maxi, mini
    if idx == k:
        tmp = int(''.join(map(str, res)))
        maxi = max(maxi, tmp)
        mini = min(mini, tmp)
        return
    for num in range(10):
        if not used[num] and ((arr[idx] == "<" and res[-1] < num) or (arr[idx] == ">" and res[-1] > num)):
            used[num] = True
            res.append(num)
            backtracking(idx+1)
            res.pop()
            used[num] = False


for i in range(10):
    res = [i]
    used = [False] * 10
    used[i] = True
    backtracking(0)
if len(str(maxi)) == k:
    maxi = "0"+str(maxi)
if len(str(mini)) == k:
    mini = "0"+str(mini)
print(maxi)
print(mini)