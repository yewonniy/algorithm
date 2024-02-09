n,m = (input()).split()
m = int(m)
n = int(n)

board = list()
chess = list()

min_change = 33

for i in range(0,n):
    board.append(list(input()))
for i in range(0,8):
    chess.append([0,0,0,0,0,0,0,0])

for i in range(0,n-7):
    for j in range(0,m-7):
        for p in range(0,8):
            chess[p] = board[p+i][0+j:j+8]
        change_a = 0
        change_b = 0
        for h in range(0,4):
            for q in range(0,4):
                #처음꺼가 black (chess[0][0] == 'B')
                    if chess[2*h+1][2*q]!='W':
                        change_a+=1
                    if chess[2*h+1][2*q+1]!='B':
                        change_a+=1
                    if chess[2*h][2*q]!="B":
                        change_a+=1
                    if chess[2*h][2*q+1]!="W":
                        change_a+=1
                #처음꺼가 white
                    if chess[2*h+1][2*q]!='B':
                        change_b+=1
                    if chess[2*h+1][2*q+1]!='W':
                        change_b+=1
                    if chess[2*h][2*q]!="W":
                        change_b+=1
                    if chess[2*h][2*q+1]!="B":
                        change_b+=1
        if change_a < min_change:
            min_change = change_a
        if change_b < min_change:
            min_change = change_b
print(min_change)