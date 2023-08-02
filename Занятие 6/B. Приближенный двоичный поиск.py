def bin_search(x, y):
    left = 0
    right = len(x) - 1
    while right - left > 1:
        m = (left + right) // 2
        if x[m] >= y:
            right = m
        else:
            left = m
    if abs(x[left] - y) == abs(x[right] - y):
        return min(x[left], x[right])
    elif abs(x[left] - y) > abs(x[right] - y):
        return x[right]
    else:
        return x[left]


n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
for i in b:
    print(bin_search(a, i))
