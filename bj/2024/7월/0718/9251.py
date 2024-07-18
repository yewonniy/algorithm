str1 = list(input())
str2 = list(input())

dy = [[0] * len(str2) for _ in range(len(str1))]


for i in range(len(str1)):
    for j in range(len(str2)):
        if i == 0:
            if str1[i] == str2[j]:
                dy[i][j] = 1
            else:
                dy[i][j] = dy[i][j-1]
        else:
            if str1[i] == str2[j]:
                if j == 0:
                    dy[i][j] = dy[i - 1][j] + 1
                else:
                    dy[i][j] = max(dy[i][j - 1], dy[i - 1][j] + 1)
            else:
                if j == 0:
                    dy[i][j] = dy[i-1][j]
                else:
                    dy[i][j] = max(dy[i-1][j], dy[i][j-1])
print(dy)
print(max(dy[-1]))



# ACAYKP
# CAPCAK