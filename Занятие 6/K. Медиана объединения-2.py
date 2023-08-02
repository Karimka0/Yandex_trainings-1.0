def posl(x1, d1, a, c, m, L):
    X = [x1]
    d = d1
    for i in range(L-1):
        x = X[i] + d
        X.append(x)
        d = (a * d + c) % m
    return X


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
    left, right = min(x[0], y[0]), max(x[-1], y[-1])
    while right > left:
        m = (left+right) // 2
        if f(m, x, L) + f(m, y, L) >= L:
            right = m
        else:
            left = m + 1
    return left


N, L = map(int, input().split())
A = []
for i in range(N):
    x1, d1, a, c, m = map(int, input().split())
    A.append(posl(x1, d1, a, c, m, L))
for i in range(N-1):
    for j in range(i+1, N):
        print(mediana(A[i], A[j], L))
