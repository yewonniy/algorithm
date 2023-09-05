n = int(input())
time = list(map(int, input().split()))
time.sort(reverse=True)

sum_ = 0
for i, tm in enumerate(time):
    sum_ += tm*(i+1)
print(sum_)