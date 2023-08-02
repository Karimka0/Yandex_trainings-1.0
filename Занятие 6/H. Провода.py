def check(m, k, a):
    t = 0
    for i in a:
        t += i // m
    if t >= k:
        return True
    else:
        return False


n, k = map(int, input().split())
a = []
sum = 0
for i in range(n):
    x = int(input())
    sum += x
    a.append(x)
l, r = 0, sum // k
while r > l:
    m = (l+r+1) // 2
    if check(m, k, a):
        l = m
    else:
        r = m - 1
print(l)
