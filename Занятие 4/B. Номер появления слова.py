s = open('input.txt')
dict = {}
for slovo in s.read().split():
    if slovo not in dict:
        dict[slovo] = 1
        print(0)
    else:
        print(dict[slovo])
        dict[slovo] += 1
