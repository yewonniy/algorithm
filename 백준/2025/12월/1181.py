n = int(input())
words = set()
for _ in range(n):
    words.add(input())
w = list(words)
w.sort(key=lambda x: (len(x), x))
for x in w:
    print(x)