n = int(input())
word = list()

def sorting_list(list_):
    new_list = sorted(list_)
    return new_list

for i in range(0, n):
    word.append(None)
    word[i] = input()

length_ordered = sorted(word, key=len)

n_list = list()

index = 0

for i in range(0, n):
    for j in range(i + 1, n - i - 1):
        if len(length_ordered[i]) == len(length_ordered[i + j]):
            index = i + j
            i = i + j
        else:
            break
    if index != 0:
        x = 0
        for k in range(i, index + 1):
            new_list = n_list.append(length_ordered[k])
        partial_list = sorting_list(new_list)

        for k in range(i, index + 1):
            length_ordered[k] = partial_list[x]
            x += 1
    index = 0