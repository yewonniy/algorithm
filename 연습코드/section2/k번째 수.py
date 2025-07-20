t = int(input())
for i in range(t):
    n, s, e, k = map(int, input().split())
    arr = list(map(int, input().split()))[s-1:e]  # 이 arr 속 숫자들 중 s ~ e 번째 수를 오름차순 정렬 -> k번째 수 출력
    arr.sort()
    print(arr[k-1])