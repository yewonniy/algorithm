# 예제 입력을 기반으로 다각형 정의
# 입력 받기
material = input().split()
xy_list = []
for i in range(len(material)):
    x = input().split()
    y = input().split()
    xy_list.append([])
    for j in range(len(x)):
        new = [x[j], y[j]]
        xy_list[i].append(new)


# 예시 코드에서 제공된 함수들을 다시 정의
def LR(A, B, C):
    result = (A[0] * B[1] - A[1] * B[0]) + (B[0] * C[1] - B[1] * C[0]) + (C[0] * A[1] - C[1] * A[0])
    if result > 0:
        return "Left"
    elif result < 0:
        return "Right"
    else:
        return "Same"


def cross(A, B, C, D):
    return LR(A, B, C) != LR(A, B, D) and LR(C, D, A) != LR(C, D, B)


# 교차점을 찾는 함수 수정
def find_intersection(A, B, C, D):
    a1 = B[1] - A[1]
    b1 = A[0] - B[0]
    c1 = a1 * A[0] + b1 * A[1]
    a2 = D[1] - C[1]
    b2 = C[0] - D[0]
    c2 = a2 * C[0] + b2 * C[1]
    determinant = a1 * b2 - a2 * b1
    if determinant == 0:
        return None  # 선분이 평행함
    x = (b2 * c1 - b1 * c2) / determinant
    y = (a1 * c2 - a2 * c1) / determinant
    if min(A[0], B[0]) <= x <= max(A[0], B[0]) and min(A[1], B[1]) <= y <= max(A[1], B[1]) and min(C[0], D[0]) <= x <= max(C[0], D[0]) and min(C[1], D[1]) <= y <= max(C[1], D[1]):
        return (x, y)
    return None


# 모든 다각형의 변을 순회하며 교차점을 찾음
intersection_points = []
for i, poly1 in enumerate(xy_list):
    for j, poly2 in enumerate(xy_list):
        if i < j:  # 중복 계산 방지
            for k in range(len(poly1)):
                for l in range(len(poly2)):
                    A, B = poly1[k], poly1[(k + 1) % len(poly1)]
                    C, D = poly2[l], poly2[(l + 1) % len(poly2)]
                    if cross(A, B, C, D):
                        intersection = find_intersection(A, B, C, D)
                        if intersection:
                            intersection_points.append(intersection)

# 중복된 교차점 제거
unique_intersection_points = list(set(intersection_points))


# 겹치는 영역의 꼭짓점을 사용하여 다각형의 넓이를 계산하는 함수
def polygon_area(vertices):
    area = 0.0
    n = len(vertices)
    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[j][0] * vertices[i][1]
    return abs(area) / 2.0


# 겹치는 영역을 형성하는 꼭짓점이 필요
# 예제에서는 회색 영역을 나타내는 꼭짓점이 주어짐
intersecting_area = polygon_area(unique_intersection_points)

# 반올림하여 출력
rounded_area = round(intersecting_area)
print(rounded_area)
