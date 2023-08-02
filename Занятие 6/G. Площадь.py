n = int(input())
m = int(input())
t = int(input())
l, r = 0, t // max(n, m)
while r > l:
    d = (l + r + 1) // 2
    if 2 * d * (m+n-2*d) <= t and (n-2*d) >= 0 and (m-2*d) >= 0:
        l = d
    else:
        r = d - 1
print(l)
