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


def tree_bypass(tree):
    if tree[1] != -1:
        tree_bypass(tree[1])
        print(tree[0])
        if tree[2] != -1:
            tree_bypass(tree[2])
        return
    elif tree[1] == -1:
        print(tree[0])
        if tree[2] != -1:
            tree_bypass(tree[2])
        return


L1 = list(map(int, input().split()))
bintree = [L1[0], -1, -1]
for i in range(1, len(L1) - 1):
    add(bintree, L1[i])
tree_bypass(bintree)
