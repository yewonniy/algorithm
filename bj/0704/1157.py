word = input()
max_cnt = 0
max_word = 0
double = 0

cnt_list = list(0 for i in range(0, 26))

for i in range(65, 91):
    capital = chr(i)
    small = chr(i+32)

    cnt_word = word.count(capital) + word.count(small)
    cnt_list[i - 65] = cnt_word
    if max_cnt <= cnt_word:
        max_cnt = cnt_word
        max_word = i

for j in range(0, 26):
    if cnt_list[max_word-65] == cnt_list[j] and max_word-65 != j:
        double = 1

if double == 1:
    print("?")
else:
    print(chr(max_word))