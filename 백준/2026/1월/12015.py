from bisect import bisect_left

n = int(input()) # 백만
arr = list(map(int, input().split()))
LIS_arr = [arr[0]]

for item in arr:
    if LIS_arr[-1] < item:
        LIS_arr.append(item)
    else:
        idx = bisect_left(LIS_arr, item)
        # bisect_left의 의미(What)
        # 이 함수에게 lis_arr과 item을 던져주면, 함수는 내부적으로 이런 질문을 던집니다.
        # "야, lis_arr은 이미 정렬되어 있잖아? 이 순서를 망가뜨리지 않으면서 item을 끼워 넣으려면 몇 번 인덱스에 넣어야 해?"
        LIS_arr[idx] = item
print(len(LIS_arr))