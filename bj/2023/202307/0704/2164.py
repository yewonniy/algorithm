N = int(input())
card_list = list()
last_number = 0
k=0

for i in range(0,N):
    card_list[i] = str(i+1)

for i in range(0,N-2):
    card_list[N + i] = card_list[2 * k + 1]
    k = k+1

for i in range(0, len(card_list)):
    if card_list[len(card_list)-1-i] != "0":
        last_number = len(card_list)-1-i
        break
print(card_list[last_number])
