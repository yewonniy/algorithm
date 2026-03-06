# 선거구 인구 차이 최소값
import sys
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]  # n*n (최대 400)
tot = 0
for x in arr:
    tot += sum(x)

# 1번 선 : (x, y) -> (+1 ~ d1, -1 ~ d1) -> 끝점 : start3
# 2번 선 : (x, y) -> (+1 ~ d2, +1 ~ d2) -> 끝점: start4
# 3번 선 : (start3[0], start3[1]) -> (+1 ~ d2, +1 ~ d2)
# 4번 선 : (start4[0], start4[1]) -> (+1 ~ d1, -1 ~ d1) -> 3번 선의 끝점과 동일
# d1 = 1 ~ y, d2 = 1 ~ n
answer = float('inf')
for a in range(n):
    for b in range(n):  # 최대 400번 반복
        # (x, y)가 기준점
        for d1 in range(1, n):
            for d2 in range(1, n):
                x, y = a, b
                if (x+d1+d2 >= n) or not(0 <= y-d1 < y+d2 < n): break
                # 1번 선 구획
                cnt1, cnt2 = 0, 0
                for i in range(x):
                    cnt1 += sum(arr[i][0:y+1])
                for i in range(x):
                    cnt2 += sum(arr[i][y+1:n])
                start3, start4, end3 = [0, 0], [0, 0], [0, 0]
                for i in range(1, d1+1):
                    xx, yy = x+i, y-i
                    cnt1 += sum(arr[xx-1][0:yy+1])
                    start3 = [xx, yy]
                # 2번 선 구획
                for i in range(d2+1):
                    xx, yy = x+i, y+i
                    if yy + 1 < n:
                        cnt2 += sum(arr[xx][yy+1:n])
                    start4 = [xx, yy]
                x, y = start3
                cnt3 = 0
                for i in range(d2+1):
                    xx, yy = x+i, y+i
                    cnt3 += sum(arr[xx][0:yy])
                    end3 = [xx, yy]
                for i in range(end3[0]+1, n):
                    cnt3 += sum(arr[i][0:end3[1]])
                x, y = start4
                cnt4 = 0
                for i in range(1, d1+1):
                    xx, yy = x+i, y-i
                    if yy+1 < n:
                        cnt4 += sum(arr[xx][yy+1:n])
                for i in range(end3[0]+1, n):
                    cnt4 += sum(arr[i][end3[1]:n])
                cnt5 = tot - (cnt1+cnt2+cnt3+cnt4)
                answer = min(answer, (max(cnt1,cnt2,cnt3,cnt4,cnt5) - min(cnt1,cnt2,cnt3,cnt4,cnt5)))
print(answer)
