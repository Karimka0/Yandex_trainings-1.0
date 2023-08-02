n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
i = j = 0
min_r = 10**7
min_i = min_j = -1
for k in range(m+n):
    if abs(a[i]-b[j]) < min_r:
        min_r = abs(a[i]-b[j])
        min_i = i
        min_j = j
        if min_r == 0:
            break
    if a[i] > b[j] and j < (m-1):
        j += 1
    elif a[i] < b[j] and i < (n-1):
        i += 1
print(a[min_i], b[min_j])
