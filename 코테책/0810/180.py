n = int(input())

std = []
for i in range(n):
    student = input().split()
    std.append((student[0], int(student[1])))

low_std = sorted(std, key = lambda data : data[1])

for i in range(n):
    print(low_std[i][0], end=' ')