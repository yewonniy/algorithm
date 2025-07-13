# 파라메트릭 서치 -> 이진 탐색을 반복문으로 구현할 것

n, m =  map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)

# 이진 탐색 시작
result = 0
while start<=end:
    total = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid:
            total += (x - mid)
    if total < m: # 좀 더 잘라야 할 때
        end = mid - 1
    else: # 좀 덜 잘라도 될 때
        result = mid # 최대한 덜 잘랐을 때가 정답이므로 여기에 기록
        start = mid + 1

print(result)