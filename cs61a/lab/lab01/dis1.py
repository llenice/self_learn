def unique_digits(n):
    """Return the number of unique digits in positive integer n.

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(101) # 0 and 1
    2
    """
    "*** YOUR CODE HERE ***"
    cnt=[0]*10
    t=0
    while n/10 > 0:
        digit=n%10
        n//=10
        cnt[digit]+=1
    for i in range(10):
        if cnt[i]!=0:
            t+=1
    return t

def has_digit(n, k):
    """Returns whether k is a digit in n.

    >>> has_digit(10, 1)
    True
    >>> has_digit(12, 7)
    False
    """
    assert k >= 0 and k < 10
    "*** YOUR CODE HERE ***"
    arrary=[]
    while n/10>0:
        arrary.append(n%10)
        n//=10
    for i in range(len(arrary)):
        if k==arrary[i]:
            return True
    return False