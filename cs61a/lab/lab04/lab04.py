from math import sqrt
from ADT import (
    make_city,
    get_name,
    get_lat,
    get_lon,
    tree,
    label,
    branches,
    is_leaf,
    print_tree,
)

# ANSWER QUESTION q1

# Problem 4.1.1
def fst(p):
    return p(0)


def snd(p):
    return p(1)


def pair(x, y):
    """Return a function that represents a pair.

    >>> p = pair(1, 2)
    >>> fst(p)
    1
    >>> snd(p)
    2
    """
    "*** YOUR CODE HERE ***"
    def f(n):
        if n==0:
            return x
        elif n==1:
            return y
    return f

def change_fst(p, v):
    """Change pair p's first element into v and return it.

    >>> p = pair(1, 2)
    >>> fst(p)
    1
    >>> snd(p)
    2
    >>> p = change_fst(p, 3)
    >>> fst(p)
    3
    >>> snd(p)
    2
    """
    "*** YOUR CODE HERE ***"
    u=snd(p)
    return pair(v,u)


def change_snd(p, v):
    """Change pair p's second element into v and return it.

    >>> p = pair(1, 2)
    >>> fst(p)
    1
    >>> snd(p)
    2
    >>> p = change_snd(p, 3)
    >>> fst(p)
    1
    >>> snd(p)
    3
    """
    "*** YOUR CODE HERE ***"
    u=fst(p)
    return pair(u,v)


# Problem 4.1.2.1
def distance(city1, city2):
    """
    >>> city1 = make_city('city1', 0, 1)
    >>> city2 = make_city('city2', 0, 2)
    >>> distance(city1, city2)
    1.0
    >>> city3 = make_city('city3', 6.5, 12)
    >>> city4 = make_city('city4', 2.5, 15)
    >>> distance(city3, city4)
    5.0
    """
    "*** YOUR CODE HERE ***"
    x1,y1=get_lat(city1),get_lon(city1)
    x2,y2=get_lat(city2),get_lon(city2)
    return sqrt((x2-x1)**2+(y2-y1)**2)

# Problem 4.1.2.2
def closer_city(lat, lon, city1, city2):
    """
    Returns the name of either city1 or city2, whichever is closest to
    coordinate (lat, lon).

    >>> berkeley = make_city('Berkeley', 37.87, 112.26)
    >>> stanford = make_city('Stanford', 34.05, 118.25)
    >>> closer_city(38.33, 121.44, berkeley, stanford)
    'Stanford'
    >>> bucharest = make_city('Bucharest', 44.43, 26.10)
    >>> vienna = make_city('Vienna', 48.20, 16.37)
    >>> closer_city(41.29, 174.78, bucharest, vienna)
    'Bucharest'
    """
    "*** YOUR CODE HERE ***"
    des=make_city('city0',lat,lon)
    if distance(des,city1) < distance(des,city2) :
        return get_name(city1)
    else:
        return get_name(city2)

# Problem 4.2.1
def deep(l):
    """Returns a deep-copy of the given list of lists.
    >>> a = [[2, 2, 2], [5, 0, 2], [5, 0, 3]]
    >>> b = deep(a)
    >>> b
    [[2, 2, 2], [5, 0, 2], [5, 0, 3]]
    >>> a is b
    False
    >>> a[0] is b[0]
    False
    >>> a[1] is b[1]
    False
    >>> a[2] is b[2]
    False
    >>> len(a) == len(b)
    True
    """
    "*** YOUR CODE HERE ***"
    b=[]
    for i in range(len(l)):
        b.append(l[i][:])
    return b


# Problem 4.2.2
def my_reverse(l):
    """Returns a new list that contains the exact same elements in l with reversed order.
    >>> a = ['S', 'I', 'C', 'P']
    >>> a is my_reverse(a) # the returned list is newly created
    False
    >>> my_reverse(my_reverse(a)) == a # reverse twice equals to the original list
    True
    >>> my_reverse(a)
    ['P', 'C', 'I', 'S']
    >>> a
    ['S', 'I', 'C', 'P']
    """
    "*** YOUR CODE HERE ***"
    return l[::-1]

# Problem 4.2.3
def my_split(f, l):
    """Splits the list into a pair of lists according to predicate f.
    >>> my_split(lambda x: True, [1, 2, 3, 4]) # All elements from l conforms to the predicate
    ([1, 2, 3, 4], [])
    >>> my_split(lambda x: x % 2 == 0, [1, 2, 3, 4]) # Split into even and odd numbers
    ([2, 4], [1, 3])
    >>> my_split(lambda x: x < 5, [3, 1, 4, 1, 5, 9, 2])
    ([3, 1, 4, 1, 2], [5, 9])
    >>> my_split(lambda x: not x, [True, False, True, True]) # There might be things other than integers
    ([False], [True, True, True])
    >>> is_ldx = lambda x: not x.startswith('24')
    >>> studentIDs = ['24122', '22122', '502024', '24183']
    >>> ldx, xdx = my_split(is_ldx, studentIDs)
    >>> ldx
    ['22122', '502024']
    >>> studentIDs # You should not mutate the original list
    ['24122', '22122', '502024', '24183']
    """
    "*** YOUR CODE HERE ***"
    split0,split1=[],[]
    for i in range(len(l)):
        if f(l[i]) :
            split0.append(l[i])
        else: 
            split1.append(l[i])
    return split0,split1


# Problem 4.3.1
def preorder(t):
    """Return a list of the entries in this tree in the order that they
    would be visited by a preorder traversal (see problem description).

    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> preorder(numbers)
    [1, 2, 3, 4, 5, 6, 7]
    >>> preorder(tree(2, [tree(4, [tree(6)])]))
    [2, 4, 6]
    """
    "*** YOUR CODE HERE ***"
    res=[label(t)]
    for i in branches(t) :
        res.extend(preorder(i))
    return res



# Problem 4.3.2
def nut_finder(t):
    """Returns True if t contains a node with the value 'nut' and
    False otherwise.

    >>> scrat = tree('nut')
    >>> nut_finder(scrat)
    True
    >>> sproul = tree('roots', [tree('branch1', [tree('leaf'), tree('nut')]), tree('branch2')])
    >>> nut_finder(sproul)
    True
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> nut_finder(numbers)
    False
    >>> t = tree(1, [tree('nut',[tree('not nut')])])
    >>> nut_finder(t)
    True
    """
    "*** YOUR CODE HERE ***"
    labels=preorder(t)
    for i in labels:
        if i=='nut' :
            return True
    return False


# Problem 4.3.3
def sprout_leaves(t, values):
    """Sprout new leaves containing the data in values at each leaf in
    the original tree t and return the resulting tree.

    >>> t1 = tree(1, [tree(2), tree(3)])
    >>> print_tree(t1)
    1
      2
      3
    >>> new1 = sprout_leaves(t1, [4, 5])
    >>> print_tree(new1)
    1
      2
        4
        5
      3
        4
        5

    >>> t2 = tree(1, [tree(2, [tree(3)])])
    >>> print_tree(t2)
    1
      2
        3
    >>> new2 = sprout_leaves(t2, [6, 1, 2])
    >>> print_tree(new2)
    1
      2
        3
          6
          1
          2
    """
    "*** YOUR CODE HERE ***"
    
    if is_leaf(t):  # 如果是叶子节点
        new_branches = [tree(value) for value in values]  # 为每个 value 创建一个新叶子节点
        return tree(label(t), new_branches)  # 返回新树
    else:  # 如果不是叶子节点
        new_branches = [sprout_leaves(child, values) for child in branches(t)]  # 递归处理子节点
        return tree(label(t), new_branches)  # 返回新树   

def insert_items(lst, entry, elem):
    """
    >>> test_lst = [1, 5, 8, 5, 2, 3]
    >>> new_lst = insert_items(test_lst, 5, 7)
    >>> new_lst
    [1, 5, 7, 8, 5, 7, 2, 3]
    >>> large_lst = [1, 4, 8]
    >>> large_lst2 = insert_items(large_lst, 4, 4)
    >>> large_lst2
    [1, 4, 4, 8]
    >>> large_lst3 = insert_items(large_lst2, 4, 6)
    >>> large_lst3
    [1, 4, 6, 4, 6, 8]
    >>> large_lst3 is large_lst
    True
    """
    "*** YOUR CODE HERE ***"
    i=len(lst)-1
    while i:
        if lst[i]==entry :
            lst.insert(i+1,elem)
        i-=1
    return lst