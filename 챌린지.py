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
            print("Cross")
            return True
    return False


def slope(A, B):  # 기울기
    if A[0] == B[0]:
        return float("inf")
    return (B[1] - A[1]) / (B[0] - A[0])


def dist(A, B):  # A, B 두 점 사이의 거리
    return ((B[0] - A[0]) ** 2 + (B[1] - A[1]) ** 2) ** 0.5


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

for i in xy_list:
    print(i)


def find_intersection(A, B, C, D):
    # 선분 AB와 CD의 교차점을 찾습니다.
    # A와 B는 첫 번째 선분의 끝점이고, C와 D는 두 번째 선분의 끝점입니다.
    # 각 선분은 (x, y) 좌표로 표현된 두 점으로 구성됩니다.

    # 선분 AB의 기울기와 y절편을 계산합니다.
    a1 = B[1] - A[1]
    b1 = A[0] - B[0]
    c1 = a1 * A[0] + b1 * A[1]

    # 선분 CD의 기울기와 y절편을 계산합니다.
    a2 = D[1] - C[1]
    b2 = C[0] - D[0]
    c2 = a2 * C[0] + b2 * C[1]

    # 선분이 평행한 경우 교차점이 없습니다.
    determinant = a1 * b2 - a2 * b1
    if determinant == 0:
        return None

    # 교차점을 계산합니다.
    x = (b2 * c1 - b1 * c2) / determinant
    y = (a1 * c2 - a2 * c1) / determinant

    # 교차점이 두 선분 모두에 속하는지 확인합니다.
    # 선분 AB에 속하는지 확인합니다.
    if min(A[0], B[0]) <= x <= max(A[0], B[0]) and min(A[1], B[1]) <= y <= max(A[1], B[1]):
        # 선분 CD에 속하는지 확인합니다.
        if min(C[0], D[0]) <= x <= max(C[0], D[0]) and min(C[1], D[1]) <= y <= max(C[1], D[1]):
            return (x, y)
    # 교차점이 선분에 속하지 않는 경우입니다.
    return None


# 모든 변에 대해 교차점을 찾습니다.
intersection_points = []
for i in range(len(xy_list)):
    for j in range(i+1, len(xy_list)):
        for k in range(len(xy_list[i])):
            A, B = xy_list[i][k], xy_list[i][(k+1) % len(xy_list[i])]
            for l in range(len(xy_list[j])):
                C, D = xy_list[j][l], xy_list[j][(l+1) % len(xy_list[j])]
                if cross(A, B, C, D):
                    # 교차점을 찾습니다.
                    intersection = find_intersection(A, B, C, D)
                    if intersection:
                        intersection_points.append(intersection)
intersection_points = list(set(intersection_points))

# 겹치는 꼭지점
# ex) vertices = [(-1.7, -0.7), (-1, -1), (2.4, -1), (2.6, 1), (1, 2)]

# Function to calculate the area of a polygon given its vertices
def polygon_area(vertices): # 겹치는 영역 계산
    # Initialize area
    area = 0.0

    # Calculate the area using the Shoelace formula
    for i in range(len(vertices)):
        j = (i + 1) % len(vertices)
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[j][0] * vertices[i][1]
    area = abs(area) / 2.0

    return area


# Calculate the area of the polygon formed by the intersecting vertices
intersecting_area = polygon_area(intersection_points)

# Since we need to round to the nearest integer
rounded_area = round(intersecting_area)
print(rounded_area) # 결과!



