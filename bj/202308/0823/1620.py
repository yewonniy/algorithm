import sys
n, m = map(int, input().split())
exp = []
for i in range(n):
    exp.append(sys.stdin.readline().rstrip())

problem = []
for i in range(m):
    x = sys.stdin.readline().rstrip()
    if (65 <= ord(x[0]) <= 90) or (65 <= ord(x[1]) <= 90):
        problem.append(x)
    else:
        problem.append(int(x))

for i in range(m):
    if type(problem[i]) == int:
        print(exp[problem[i]-1])
    else:
        print(exp.index(problem[i])+1)
