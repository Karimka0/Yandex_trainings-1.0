n = int(input())
ty = []
for i in range(n):
    x, y = map(int, input().split())
    ty.append(y)
pod_arr = [0] * len(ty)
for i in range(1, len(ty)):
    if ty[i] - ty[i-1] > 0:
        pod_arr[i] = pod_arr[i-1] + ty[i] - ty[i-1]
    else:
        pod_arr[i] = pod_arr[i-1]
sp_arr = [0] * len(ty)
for i in range(1, len(ty)):
    if ty[i-1] - ty[i] > 0:
        sp_arr[i] = sp_arr[i-1] + ty[i-1] - ty[i]
    else:
        sp_arr[i] = sp_arr[i-1]
m = int(input())
for i in range(m):
    s, f = map(int, input().split())
    if s < f:
        print(pod_arr[f-1]-pod_arr[s-1])
    else:
        print(sp_arr[s-1]-sp_arr[f-1])
