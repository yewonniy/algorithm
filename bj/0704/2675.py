T = int(input())
new_list = list()
word = ""

for i in range(0, T):
    R, S = input().split()
    int_R = int(R)
    list_S = list(S)

    for j in range(0, len(list_S)):
        for k in range(0, int_R):
            word = word + list_S[j]
    new_list.append(word)
    word = ""

for j in range(0, len(new_list)):
    print(new_list[j])