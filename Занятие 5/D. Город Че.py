n, r = map(int, input().split())
d = list(input().split())
first, last, ans = 0, 1, 0
while last < n and first < n - 1:
    if int(d[last]) - int(d[first]) <= r:
        last += 1
    else:
        ans += n - last
        first += 1
print(ans)
