def f(c, x, L):
    if c < x[0]:
        return 0
    l, r = 0, L-1
    while r > l:
        m = (r+l+1) // 2
        if c >= x[m]:
            l = m
        else:
            r = m - 1
    return r + 1


def mediana(x, y, L):
    left, right = -30001, 30001
    while right > left:
        m = (left+right) // 2
        if f(m, x, L) + f(m, y, L) >= L:
            right = m
        else:
            left = m + 1
    return left


N, L = map(int, input().split())
a = []
for i in range(N):
    a.append(list(map(int, input().split())))
for i in range(N):
    for j in range(i+1, N):
        p = a[i]
        q = a[j]
        print(mediana(p, q, L))
