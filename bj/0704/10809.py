S = list(input())
S_list = list(-1 for i in range(0, 26))

for i in range(0, len(S)):
    for j in range(97, 123):
        if chr(j) == S[i] and S_list[j-97] == -1:
            S_list[j-97] = i
            break
for i in range(0, 26):
    print(S_list[i], end=' ')

