N = int(input())
word_list = list()
max_length = 0
min_length = 51

for i in range(0, N):
    word = input()
    if word not in word_list:
        word_list.append(word)
    if len(word) < min_length:
        min_length = len(word)
    if len(word) > max_length:
        max_length = len(word)

same_length = list()
for i in range(min_length, max_length+1):
    for j in word_list:
        if len(j) == i:
            same_length.append(j)
    same_length.sort()
    if len(same_length) > 0:
        print(*same_length, sep='\n')
    same_length.clear()
