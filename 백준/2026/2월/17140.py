# 수의 등장 횟수 (작-> 큰) 같으면, 수 itself 크기 (작->큰)
import heapq
r, c, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]
# 배열 A[r-1][c-1]가 k가 되면 끝!
row, column, time = 3, 3, 0 # x= 행 개수

def row_sort(arr):
    max_column = 0
    for i, row in enumerate(arr):
        dic = dict()
        tmp = []
        q = []
        for num in row:
            if num != 0:
                dic[num] = dic.get(num, 0) + 1
        for key in dic:
            heapq.heappush(q, (dic[key], key))
        while q:
            cnt, num = heapq.heappop(q)
            if len(tmp) < 100:
                tmp.append(num)
            if len(tmp) < 100:
                tmp.append(cnt)
        arr[i] = tmp
        max_column = max(max_column, len(tmp))
    for row in arr:
        while len(row) < max_column:
            row.append(0)
    return max_column, arr


while True:
    if time > 100:
        print(-1)
        break
    if r-1 < row and c-1 < column and A[r-1][c-1] == k:
        print(time)
        break
    # 계속 연산 수행
    if row >= column:  # r 연산 수행 -> arr의 모든 행 정렬
        column, arr = row_sort(A)
    else:
        tmp = list(map(list, zip(*A)))
        row, res = row_sort(tmp)
        A = list(map(list, zip(*res)))
    time += 1
