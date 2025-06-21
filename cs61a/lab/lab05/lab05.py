# ANSWER QUESTION wwpd

def takeWhile(t, p):
    """Take elements from t until p is not satisfied.

    >>> s = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> list(takeWhile(s, lambda x: x == 10))
    [10]
    >>> s2 = iter([1, 1, 2, 3, 5, 8, 13])
    >>> list(takeWhile(s2, lambda x: x % 2 == 1))
    [1, 1]
    >>> s = iter(['a', '', 'b', '', 'c'])
    >>> list(takeWhile(s, lambda x: x != ''))
    ['a']
    >>> list(takeWhile(s, lambda x: x != ''))
    ['b']
    >>> next(s)
    'c'
    """
    "*** YOUR CODE HERE ***"
    # 停止 yield 的方法:
    # raise StopIteration
    # return
    for x in t:
        if not p(x):
            return
        yield x


def backAndForth(t):
    """Yields and skips elements from iterator t, back and forth.

    >>> list(backAndForth(iter([1, 2, 3, 4, 5, 6, 7, 8, 9])))
    [1, 4, 5, 6]
    >>> list(backAndForth(iter([1, 2, 2])))
    [1]
    >>> # generators allow us to represent infinite sequences!!!
    >>> def naturals():
    ...     i = 0
    ...     while True:
    ...         yield i
    ...         i += 1
    >>> m = backAndForth(naturals())
    >>> [next(m) for _ in range(9)]
    [0, 3, 4, 5, 10, 11, 12, 13, 14]
    """
    "*** YOUR CODE HERE ***"
    # 思路:
    # 1. 现在是第几轮：round
    # 2. 现在是第round轮的第几个：i
    # 3. round是偶数 => 跳过
    # 4. round是奇数 => yield
    i,round=0,1
    for x in t:
        i+=1
        if round%2 ==1:
            yield x
        if i == round :
            i=0
            round+=1






def scale(it, multiplier):
    """Yield elements of the iterable it scaled by a number multiplier.

    >>> m = scale(iter([1, 5, 2]), 5)
    >>> type(m)
    <class 'generator'>
    >>> list(m)
    [5, 25, 10]
    >>> # generators allow us to represent infinite sequences!!!
    >>> def naturals():
    ...     i = 0
    ...     while True:
    ...         yield i
    ...         i += 1
    >>> m = scale(naturals(), 2)
    >>> [next(m) for _ in range(5)]
    [0, 2, 4, 6, 8]
    """
    "*** YOUR CODE HERE ***"
    for k in it :
        yield k*multiplier
    #1. yield from map(lambda x: x * multiplier, it)
    #2. list(map(f, lsy))
    #3. return tree(f(label(t)), [map_tree(f, b) for b in branches(t)])



def merge(a, b):
    """Merge two generators that are in increasing order and without duplicates.
    Return a generator that has all elements of both generators in increasing
    order and without duplicates.

    >>> def sequence(start, step):
    ...     while True:
    ...         yield start
    ...         start += step
    >>> a = sequence(2, 3) # 2, 5, 8, 11, 14, ...
    >>> b = sequence(3, 2) # 3, 5, 7, 9, 11, 13, 15, ...
    >>> result = merge(a, b) # 2, 3, 5, 7, 8, 9, 11, 13, 14, 15
    >>> [next(result) for _ in range(10)]
    [2, 3, 5, 7, 8, 9, 11, 13, 14, 15]
    """
    "*** YOUR CODE HERE ***"
    ka, kb=next(a), next(b)
    while True :
        if ka < kb :
            yield ka
            ka = next(a)
        elif ka==kb:
            yield ka
            ka,kb=next(a), next(b)
        elif ka>kb:
            yield kb
            kb=next(b)

 
        

def hailstone(n):
    """Return a generator that outputs the hailstone sequence.

    >>> for num in hailstone(10):
    ...     print(num)
    10
    5
    16
    8
    4
    2
    1
    """
    "*** YOUR CODE HERE ***"
    # 1. recursion
    # hailstone(n) 表示从 n 开始的 hailstone 数列
    # hailstone(n) 的第一项就是 n
    # 若 n 是 1，结束
    # n 是奇数，从第二项起是以 n*3+1 为首的 hailstone 数列
    # n 是偶数，从第二项起是以 n//2 为首的 hailstone 数列
    yield n
    if n==1 :
        return
    if n%2 == 1:
        yield from hailstone(3*n+1)
    else :
        yield from hailstone(n//2)

    #2. 迭代 iteration
    #写一个 while 版本的算法
    # 2. 在必要的时候 yield 
    yield n
    while n!=1 :
        if n%2 ==0 :
            n=n//2
        else :
            n=3*n+1
        yield n
