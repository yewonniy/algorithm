import sys

n, m = map(int, input().split())
not_heard = []
not_seen = []
both = []

for i in range(n):
    not_heard.append(sys.stdin.readline().rstrip())
for i in range(m):
    not_seen.append(sys.stdin.readline().rstrip())

not_heard.sort()
not_seen.sort()

for x in not_heard:
    target = x
    start = 0
    end = len(not_seen) - 1
    while start <= end:
        mid = (start + end) // 2
        if not_seen[mid] == target:
            both.append(target)
            break
        elif not_seen[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
        if start > end:
            break

both.sort()
print(len(both))
for a in both:
    print(a)