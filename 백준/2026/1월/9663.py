n = int(input())
# 하나의 row엔 퀸(1)이 하나, 하나의 column에도 퀸이 하나
ans = 0


def backtracking(x, column):
    # 일단 [x][y] 위치에 퀸을 놔보고, 정답이 불가하면 undo해서 되돌아가자!
    global ans
    if x == n: # 전부 다 놓았음
        ans += 1
        return True
    # 이제 x번째 row의 몇 번 column에 퀸을 놓을까? (L-1 행까진 퀸 다 놓여져있음)
    for y in range(n):  # [x][y] 가 후보가 됨.
        if check1[y] and check2[x+y] and check3[(y-x)+n]:
            check1[y] = False
            check2[x+y] = False
            check3[(y-x)+n] = False
            backtracking(x+1, y)
            check1[y] = True
            check2[x+y] = True
            check3[(y-x)+n] = True


for y in range(n):
    # [0][y]에 첫번째 퀸
    check1 = [True] * n  # 세로로 겹치는지 검증
    check2 = [True] * (2*n)  # 왼쪽 아래 대각선으로 겹치는지 검증
    check3 = [True] * (3*n)  # 오른쪽 아래 대각선
    check1[y] = False
    check2[y] = False
    check3[y+n] = False
    backtracking(1, y)
print(ans)