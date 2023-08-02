n, x, y = map(int, input().split())
left, right = 0, min(x, y) * (n-1)
while right > left:
    m = (right+left) // 2
    if m//x + m//y >= n - 1:
        right = m
    else:
        left = m + 1
print(left + min(x, y))
