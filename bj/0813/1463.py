n = int(input())
ter_num = 665
cnt = 0

while True:
    ter_num += 1
    if str(ter_num).count('666') >= 1:
        cnt += 1
    if cnt == n:
        break

print(ter_num)