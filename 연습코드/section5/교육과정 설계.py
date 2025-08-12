from collections import deque

must = list(input())
n = int(input())
for k in range(1, n + 1):
    syllabus = deque(input())
    check = [False] * len(must)
    false = False
    for i in range(len(syllabus)):
        subject = syllabus.popleft()
        if subject in must:
            idx = must.index(subject)
            check[idx] = True
            for j in range(idx):
                if not check[j]:
                    false = True
                    break
        if false:
            print("#"+str(k)+" NO")
            break
    else:
        if all(check[i] for i in range(len(check))):
            print("#" + str(k) + " YES")
        else:
            print("#" + str(k) + " NO")
