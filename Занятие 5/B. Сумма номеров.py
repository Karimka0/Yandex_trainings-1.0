n, k = map(int, input().split())
a = list(map(int, input().split()))
prefix = [0] * (len(a)+1)
for i in range(1, len(a)+1):
    prefix[i] = prefix[i-1] + a[i-1]
ans_cnt = 0
l = 0
r = 1
while r < len(prefix):
    if prefix[r] - prefix[l] < k:
        r += 1
    elif prefix[r] - prefix[l] > k:
        l += 1
    else:
        ans_cnt += 1
        r += 1
print(ans_cnt)
