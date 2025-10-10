def solution(board, skill):  # board : 건물 내구도, skill: 공격/회복 스킬
    # [type, r1, c1, r2, c2, degree] -> type = 1이면 공경, 2이면 회복
    # 1) 노가다 구현
    n, m = len(board), len(board[0])
    answer = 0
    diff = [[0] * m for _ in range(n)]
    # 3중 for문의 시간복잡도를 줄이는 방법 -> IMOS 알고리즘 활용 (누적합)
    for type_, r1, c1, r2, c2, d in skill:
        degree = -d if type_ == 1 else d
        diff[r1][c1] += degree
        if c2 + 1 < m:
            diff[r1][c2 + 1] -= degree
        if r2 + 1 < n:
            diff[r2 + 1][c1] -= degree
        if r2 + 1 < n and c2 + 1 < m:
            diff[r2 + 1][c2 + 1] += degree

    # 행 누적 합
    for x in range(n):
        for y in range(1, m):
            diff[x][y] += diff[x][y - 1]
    for x in range(1, n):
        for y in range(m):
            diff[x][y] += diff[x - 1][y]

    for x in range(n):
        for y in range(m):
            board[x][y] += diff[x][y]
            if board[x][y] > 0:
                answer += 1
    return answer