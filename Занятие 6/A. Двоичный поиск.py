def bin_search(x, y):
    left = 0
    right = len(x) - 1
    while right - left > 1:
        m = (left + right) // 2
        if x[m] >= y:
            right = m
        else:
            left = m
    if x[left] == y or x[right] == y:
        print("YES")
    else:
        print("NO")


N, K = map(int, input().split())
n = list(map(int, input().split()))
n.sort()
k = list(map(int, input().split()))
for i in k:
    bin_search(n, i)
