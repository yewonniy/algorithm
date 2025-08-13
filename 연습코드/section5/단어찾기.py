n = int(input())
dict = {}
for i in range(n):
    word = input()
    if dict.get(word):
        dict[word] += 1
    else:
        dict[word] = 1

for i in range(n-1):
    w = input()
    dict[w] -= 1
    if dict[w] == 0:
        dict.pop(w)
print(list(dict)[0])

