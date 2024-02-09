# 예제 입력을 기반으로 다각형 정의
# 입력 받기
# X Y Z
# -2 -5 -1 4 4
# 6 1 -1 -1 3
# -1 -4 -4 2 3
# 3 -1 -4 -4 5
# 1 -3 2 6
# 2 -2 -3 -1
material = input().split() # 물질 이름
xy_list = []
for i in range(len(material)):
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    xy_list.append([])
    for j in range(len(x)):
        new = [x[j], y[j]]
        xy_list[i].append(new)
    xy_list[i].append([x[0], y[0]])
# xy_list = [[(x, y), (x, y) ...], [(x, y), (x, y) ..]]


def LR(A, B, C):  # A = [0,1]
    result = (A[0] * B[1] - A[1] * B[0]) + (B[0] * C[1] - B[1] * C[0]) + (C[0] * A[1] - C[1] * A[0])
    if result > 0:
        return "Left"
    elif result < 0:
        return "Right"
    else:
        return "Same"


def cross(A, B, C, D):
    if LR(A, B, C) != LR(A, B, D):
        if LR(C, D, A) != LR(C, D, B):
            return True
    return False


def inOut(p, x, y): # p 가 볼록다각형 꼭짓점들이 들어있는 리스트고 x, y가 내부에 있는지 외부에 있는지 판단할 점
    count = 0
    for i in range(len(p)-1):
        if p[i][1] == p[i+1][1] :
            count = count
        elif p[i][1] == y and x < p[i][0]:
            if p[i+1][1] > p[i][1]:
                count += 1
        elif p[i+1][1] == y and x < p[i+1][0]:
            if p[i][1] > p[i+1][1] :
                count += 1
        else:
            if cross(p[i], p[i+1], [x, y], [100000000000, y]):
                count += 1
    return count


total_inside = 0
for x in range(-100, 101):
    for y in range(-100, 101): # (-100, -100) 부터 (100, 100)까지 모든 점에 대해서 내부, 외부 판단
        inside = 0
        for dot_list in xy_list:
            if inOut(dot_list, x, y) % 2 != 0: # 점 (x,y)가 해당 볼록 다각형 내에 있다면
                inside += 1
        if inside == len(xy_list): # 점 (x,y)가 모든 볼록 다각형의 내부에 있다면
            #print((x, y))
            total_inside += 1

print(total_inside) # 모든 다각형의 내부에 있는 격자점 개수 출력


