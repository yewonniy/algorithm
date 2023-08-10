m,n = (input()).split()
m = int(m)
n = int(n)

for i in range(m, n+1):
    find=1
    if i == 2 or i == 3:
        print(i)
    elif i != 1:
        for j in range(2, round(i**0.5)+1):
            if i%j == 0:
                find = 0
                break
        if find == 1:
            print(i)