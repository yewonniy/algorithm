A = int(input())
B = int(input())
C = int(input())

ABC = A*B*C
strABC = str(ABC)

count_list = [0 for i in range(10)]

for i in range(0, 10):
    k = str(i)
    cnt = strABC.count(k)
    count_list[i] = cnt

for i in range(0, 10):
    print(count_list[i])
