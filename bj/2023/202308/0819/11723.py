import sys

s = set()
m = int(input())
for i in range(m):
    cal = sys.stdin.readline().rstrip().split()
    if len(cal) > 1:
        cal[1] = int(cal[1])
        if cal[0] == 'add':
            s.add(cal[1])
        elif cal[0] == 'remove':
            s.discard(cal[1])
        elif cal[0] == 'check':
            if cal[1] in s:
                print(1)
            else:
                print(0)
        else:
            if cal[1] in s:
                s.discard(cal[1])
            else:
                s.add(cal[1])
    else:
        if cal[0] == 'all':
            s = set([i for i in range(1, 21)])
        else:
            s = set()