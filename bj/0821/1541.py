arr = [input()]
num = []
memo = []
last = -1

for i in range(len(arr[0])):
    if arr[0][i] == '-' or arr[0][i] == '+':
        num.append(int(arr[0][(last+1):i]))
        last = i
        num.append(arr[0][i])
num.append(int(arr[0][last+1:len(arr[0])]))

for i in range(len(num)):
    if i < len(num)-2 and num[i] == '-' and num[i+2] == '+':
        num.insert(i+1, '(')
        memo.append(i+1)
        j = 2
        index = i+5
        if i+j < len(num):
            while num[i+j] != '-':
                j += 1
                if i+j >= len(num):
                    break
                if num[i+j] == '-':
                    index = i + j
                    break
        num.insert(index, ')')
        memo.append(index)
print(num)

def plus(array, start, end):
    res = 0
    for i in range(start, end+1, +2):
        res += array[i]
    return res


final = []
close = -2
if len(memo) > 0:
    for i in range(0, len(memo), +2):
        open_ = memo[i] + 1
        for j in range(close+2, open_-1):
            final.append(num[j])
        close = memo[i+1] - 1
        final.append(plus(num, open_, close))
    if close+2 != len(num):
        for j in range(close+2, len(num)):
            final.append(num[j])
    result = final[0]
    for i in range(2, len(final), +2):
        result = result - final[i]
else:
    result = num[0]
    if '-' not in num:
        for i in range(2, len(num), +2):
            result += num[i]
    elif '+' not in num:
        for i in range(2, len(num), +2):
            result -= num[i]
    else:
        for i in range(2, len(num), +2):
            if num[i-1] == '-':
                result -= num[i]
            else:
                result += num[i]
print(result)

# 55-50+45+10+20-30-40+30-30, 50-10-10+23+23