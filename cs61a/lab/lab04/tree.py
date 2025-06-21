# def fact(n) :
#     def helper(i, res=1) :
#         if i == 1:
#             return res
#         else :
#             return helper(i-1, res*i)
#     return helper(n, 1)

# print(fact(3))‘

def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch)
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

number_tree = tree(1, [
    tree(2),
    tree(3, [
        tree(4),
        tree(5)
    ]),
    tree(6, [
        tree(7)
    ])
])

def leaves(tree):
    """Return a list containing the leaves of tree.
    >>> leaves(fib_tree(5))
    [1, 0, 1, 0, 1, 1, 0, 1]
    """
    if is_leaf(tree):
        return [label(tree)]
    else:
        return sum([leaves(b) for b in branches(tree)], [])
    
def increment_leaves(t):
    """Return a tree like t but with leaf values incremented."""
    if is_leaf(t):
        return tree(label(t) + 1)
    else :
        bs = [increment_leaves(b) for b in branches(t)]
        return tree(label(t), bs)
    
def increment(t):
    """Return a tree like t but with all node values incremented."""
    return tree(label(t) + 1, [increment(b) for b in branches(t)])

def count_paths(t, total):
    if total == label(t) :
        found=1
    else :
        found=0
    return found+([count_paths(b, total - label(t)) for b in branches(t)])


print(number_tree)
print(label(number_tree))
print(branches(number_tree))
print(is_leaf(number_tree))
print(leaves(number_tree))
print(increment_leaves(number_tree))
print(increment(number_tree))
