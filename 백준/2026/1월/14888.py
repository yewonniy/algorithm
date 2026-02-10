n = int(input())
nums = list(map(int, input().split()))
oper = list(map(int, input().split()))
op = ["+", "-", "*", "//"]


def do_operation(i, a, b):
    if i == 0:
        return a + b
    elif i == 1:
        return a - b
    elif i == 2:
        return a * b
    elif a < 0:
        return - (-a // b)
    return a // b


def backtracking(L, num):
    global mini, maxi
    if L == n:
        print("결과",num)
        maxi = max(maxi, num)
        mini = min(mini, num)
    for i in range(4):
        if oper[i] > 0:
            oper[i] -= 1
            new = do_operation(i, num, nums[L])
            backtracking(L+1, new)
            oper[i] += 1


mini = float("inf")
maxi = -(10**11)
backtracking(1, nums[0])
print(maxi)
print(mini)