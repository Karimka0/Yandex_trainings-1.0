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


def height(tree):
    if tree[1] == -1 and tree[2] == -1:
        return 1
    elif tree[1] == -1 and tree[2] != -1:
        return height(tree[2]) + 1
    elif tree[2] == -1 and tree[1] != -1:
        return height(tree[1]) + 1
    elif tree[2] != -1 and tree[1] != -1:
        return max(height(tree[1]), height(tree[2])) + 1


L1 = list(map(int, input().split()))
bintree = [L1[0], -1, -1]
for i in range(1, len(L1) - 1):
    add(bintree, L1[i])
print(height(bintree))
