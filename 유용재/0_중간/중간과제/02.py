n = int(input())
result = 0

i = 1
while True:
    result += i
    print(i, result)
    if result == n :
        print(i)
        break
    elif result < n < result + i+1:
        print(i)
        break
    else:
        i += 1
