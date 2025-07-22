word = input()
res = 0
cnt = 0
for i in range(len(word)):
    if word[i].upper() == word[i].lower(): # -> if word[i].isdecimal():
        res = res*10 + int(word[i])
print(res)

cnt = 0
for i in range(1,int(res**0.5 + 1)):
    if res % i == 0:
        if float(i) == res**0.5:
            cnt += 1
        else:
            cnt += 2
print(cnt)