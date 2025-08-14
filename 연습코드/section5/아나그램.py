word1 = list(input())
word2 = list(input())

ana = dict()
for x in word1:
    if x in ana.keys():
        ana[x] += 1
    else:
        ana[x] = 1

for x in word2:
    if x in ana.keys():
        ana[x] -= 1
    else:
        print("No")
        break
else:
    if all(v == 0 for v in ana.values()):
        print("YES")
    else:
        print("No")
