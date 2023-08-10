N = int(input())
min_box = 1001
possible = 0

for i in range(0, N//3+2): #3
    for j in range(0, N//5+2): #5kg
        if 3*i+5*j == N:
            if i+j < min_box:
                min_box = i+j
            possible=1

if possible==1:
    print(min_box)
else:
    print(-1)