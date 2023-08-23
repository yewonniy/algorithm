exp = input()
cnt_ = 0
result = 0

if "-" not in exp:
    arr = map(int, exp.split("+"))
    print(sum(arr))
else:
    arr = exp.split("-")
    for i in range(len(arr)):
        plus = []
        cnt = 0
        if '+' in arr[i]:
            if i != 0:
                temp = map(int, arr[i].split("+"))
                cnt = sum(temp)
            else:
                temp = map(int, arr[i].split("+"))
                result = sum(temp)
        else:
            if i != 0:
                result -= int(arr[i])
            else:
                result += int(arr[i])
        if cnt != 0:
            result += cnt_ - cnt
            cnt_ = 0
    print(result)