n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

first = data[n-1]
second = data[n-2]

f = m//(k+1)
f_ = m%(k+1)
s = m%k
sum = first*k*f + second*s + first*f_
print(f, s, f_, sum)