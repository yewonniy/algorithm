play = (input()).split()
play_len = len(play)
ascending = 0
descending = 0

for i in range(0, play_len-1):
    if int(play[i+1]) == (int(play[i]))+1 :
        ascending = ascending+1
    elif int(play[i+1]) == (int(play[i]))-1 :
        descending = descending+1

if ascending == play_len-1:
    print("ascending")
elif descending == play_len-1:
    print("descending")
else:
    print("mixed")