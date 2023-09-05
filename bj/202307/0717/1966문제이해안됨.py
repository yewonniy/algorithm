t = int(input()) #테스트 케이스 수
NandM = list()
priority_list = list()
priority = list()


for i in range(0,t):
    NandM.append(input())
    priority_list.append(input())

for i in range(0,t):
    cnt=0
    N = int(NandM[i].split()[0]) #문서 수
    M = int(NandM[i].split()[1]) #몇 번째로 출력되는지 궁금한 문서의 인덱스
    priority = priority_list[i].split()
    for j in range(0,N):
        for k in range(1,N):
            if priority[0] < priority[k]:
                priority.append(priority[0])
                del priority[0]
                cnt+=1
                break
    print(M-cnt)

