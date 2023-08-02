n, a, b, w, h = map(int, input().split())
left, right = 0, max(w, h)
while right > left:
    m = (right+left+1)//2
    if (w//(a+2*m)) * (h//(b+2*m)) >= n or (w//(b+2*m)) * (h//(a+2*m)) >= n:
        left = m
    else:
        right = m - 1
print(right)
