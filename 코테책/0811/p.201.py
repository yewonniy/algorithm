n, m = map(int, input().split())
rice = list(map(int, input().split()))
cnt = 0
rice.sort(reverse=True)


def rice_cut(array, start, target):
    global cnt
    while target != cnt:
        if target == cnt:
            return array[start]
        for i in range(1, n-start):
            if array[start] == array[start+i]:
                array[start+i] -= 1
                cnt += 1
            else:
                break
            if cnt == target:
                return array[start+i]
        array[start] -= 1
        cnt += 1


result = rice_cut(rice, 0, m)
print(result)