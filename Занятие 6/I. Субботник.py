def check(a, r, c, m):
    i = 0
    k = 0
    while i <= len(a) - c:
        if a[i+c-1] - a[i] <= m:
            k += 1
            i += c
        else:
            i += 1
    if k >= r:
        return True
    else:
        return False


n, r, c = map(int, input().split())
a = []
for i in range(n):
    a.append(int(input()))
a.sort()
left, right = 0, a[-1] - a[0]
while right > left:
    m = (left+right) // 2
    if check(a, r, c, m):
        right = m
    else:
         left = m + 1
print(left)
