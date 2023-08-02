a = open('input.txt')
s = a.read().split()
dict = {}
dict[s[0]] = 0
max_cnt = 0
max_str = s[0]
for i in s:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1
for i in dict:
    if dict[i] > max_cnt or (dict[i] == max_cnt and max_str > i):
        max_cnt = dict[i]
        max_str = i
print(max_str)
