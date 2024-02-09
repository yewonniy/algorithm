n = int(input())

S = []    
for i in range(0, n+1):
    new_list = []
    for j in range(0, n+1):
        new_list.append(-1)
    S.append(new_list)

for i in range(1, n+1):
    for j in range(1, i+1):
        if j == i or j == 1:
            S[i][j] = 1
        else:
            S[i][j] = S[i-1][j-1] + j*S[i-1][j]

result = 0
for i in range(2, n+1):
    result += S[n][i]

print(result)