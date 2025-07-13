n, m = map(int, input().split())
cnt = 0

index_list = []
for _ in range(n):
    index_list.append([])
m_list = []
for i in range(m):
    m_list.append(i)

for i in range(n):
    g, p = input().split()
    play = list(p)
    for j in range(m):
        if play[j] == "Y":
            index_list[i].append(j)
    cnt = max(cnt, play.count("Y"))

if cnt == 0: # 모든 게 No
    print(-1)
elif cnt == m: # 한 개의 기타로 모든 곡 연주 가능
    print(1)
else: # 계산
    # all_song = []
    # for i in range(n):
    #     all_song = list(set(all_song + index_list[i]))
    # if len(all_song) == m:
    #     print("모든 곡 가능")
    # index_list.sort()


def diff():
    for i in range(n):
        for j in range(i, n):
            diff = list(set(index_list[i]) - set(index_list[j]))


