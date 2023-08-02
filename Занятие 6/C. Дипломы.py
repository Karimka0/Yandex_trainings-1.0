w, h, n = map(int, input().split())
a, b = 0, max(w, h) * n
while b - a > 0:
    m = (a + b) // 2
    if (m//h) * (m//w) >= n:
        b = m
    else:
        a = m + 1
print(b)
