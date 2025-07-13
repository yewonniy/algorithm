# 볼록 껍질 문제
def slope(A, B):  # 기울기
    if A[0] == B[0]:
        return float("inf")
    return (B[1] - A[1]) / (B[0] - A[0])


def dist(A, B):  # A, B 두 점 사이의 거리
    return ((B[0] - A[0]) ** 2 + (B[1] - A[1]) ** 2) ** 0.5


p = [[1, 3], [0, 7], [0, 3], [-9, 3], [-3, -8], [2, 4], [8, 8], [7, 7]]

i = p.index(min(p))
p[0], p[i] = p[i], p[0]

for round in range(len(p)): # 기울기를 기준으로 점들 정렬하기
    for i in range(1, len(p) - 1):
        if slope(p[0], p[i]) > slope(p[0], p[i+1]) : # 뒤에 꺼 기울기가 더 작으면 앞에 꺼랑 바꾼다.
            p[i], p[i+1] = p[i+1], p[i]
        elif slope(p[0], p[i]) == slope(p[0], p[i+1]): # 기울기가 같으면 거리가 더 가까운 놈을 앞으로.
            if dist(p[0],p[i]) > dist(p[0], p[i+1]):
                p[i], p[i+1] = p[i+1], p[i]

stack = [p[0], p[1]]

for i in range(2, len(p)):
    while True:
        if LR(stack[-2], stack[-1], p[i]) == "Right" :
            stack.pop()
        else:
            stack.append(p[i])
            break

print(stack)
