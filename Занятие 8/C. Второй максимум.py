def add(bin_tree, element):
    if element == bin_tree[0]:
        return
    elif element < bin_tree[0]:
        if bin_tree[1] == -1:
            bin_tree[1] = [element, -1, -1]
        else:
            add(bin_tree[1], element)
    else:
        if bin_tree[2] == -1:
            bin_tree[2] = [element, -1, -1]
        else:
            add(bin_tree[2], element)


def search_max(tree):
    if tree[2] != -1:
        return search_max(tree[2])
    else:
        return tree[0]


L = list(map(int, input().split()))
L1 = L[:-1]
bintree = [L1[0], -1, -1]
for i in range(1, len(L1)):
    add(bintree, L1[i])
second_max = 0
while bintree[2] != -1:
    if bintree[1] != -1:
        second_max = max(search_max(bintree[1]), bintree[0])
    else:
        second_max = bintree[0]
    bintree = bintree[2]
else:
    if bintree[1] != -1:
        second_max = max(second_max, search_max(bintree[1]))
print(second_max)
