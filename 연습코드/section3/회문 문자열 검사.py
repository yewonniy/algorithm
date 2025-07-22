n = int(input())
# words = []
# for _ in range(n):
#     words.append(input().lower())
#
# for word in words:
#     l = len(word)
#     cnt = 0
#     for i in range(int(l//2)):
#         if word[i] == word[-(i+1)]:
#             cnt += 1
#         if cnt != i+1:
#             print("NO")
#             break
#     else:
#         print("YES")

for i in range(n):
    word = input().lower()
    if word == word[::-1]:
        print("YES")
    else:
        print("NO")