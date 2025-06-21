""" Lab 3: Recursion """

LAB_SOURCE_FILE = "lab03.py"


# ANSWER QUESTION q1

# ANSWER QUESTION q2

# ANSWER QUESTION q3


def f91(n):
    """Takes a number n and returns n - 10 when n > 100,
    returns f91(f91(n + 11)) when n ≤ 100.

    >>> f91(1)
    91
    >>> f91(2)
    91
    >>> f91(100)
    91
    """
    "*** YOUR CODE HERE ***"
    if n> 100:
        return n-10
    else :
        return f91(f91(n+11))


def is_monotone(n):
    """Returns whether n has monotone digits.
    Implement using recursion!

    >>> is_monotone(22000130)
    False
    >>> is_monotone(1234)
    True
    >>> is_monotone(24555)
    True
    >>> # Do not use while/for loops!
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(LAB_SOURCE_FILE, 'is_monotone', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n<10 :
        return True
    last_d=n%10
    sec_d=(n//10)%10
    if last_d<sec_d:
            return False
    else :
            return is_monotone(n//10)


def count_stair_ways(n):
    """Returns the number of ways to climb up a flight of
    n stairs, moving either 1 step or 2 steps at a time.
    >>> count_stair_ways(3)
    3
    >>> count_stair_ways(4)
    5
    >>> count_stair_ways(10)
    89
    """
    "*** YOUR CODE HERE ***"
    if n<=1 :
        return 1
    else :
        return count_stair_ways(n-1)+count_stair_ways(n-2)
        


def count_k(n, k):
    """Counts the number of paths to climb up a flight of n stairs,
    taking up to and including k steps at a time.
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    >>> count_k(3, 5) # Take no more than 3 steps
    4
    """
    "*** YOUR CODE HERE ***"
    if n<=1 :
        return 1
    elif n>1 and n<k:
        sum=0
        for i in range(0,n) :
            sum+=count_k(i,k)
        return sum
    else :
        sum=0
        for i in range(1,k+1):
            sum+=count_k(n-i,k)
        return sum
    # sum=0
    # for i in range (1,min(k,n)+1) :
    #      sum+=count_k(n-i, k)
    # return sum


def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    "*** YOUR CODE HERE ***"
    if m==1 or n==1 :
        return 1
    else :
        return paths(m-1,n)+paths(m,n-1)


def max_subseq(n, l):
    """
    Return the maximum subsequence of length at most l that can be found in the given number n.
    For example, for n = 20125 and l = 3, we have that the subsequences are
        2
        0
        1
        2
        5
        20
        21
        22
        25
        01
        02
        05
        12
        15
        25
        201
        202
        205
        212
        215
        225
        012
        015
        025
        125
    and of these, the maximum number is 225, so our answer is 225.

    >>> max_subseq(20125, 3)
    225
    >>> max_subseq(20125, 5)
    20125
    >>> max_subseq(20125, 6) # note that 20125 == 020125
    20125
    >>> max_subseq(12345, 3)
    345
    >>> max_subseq(12345, 0) # 0 is of length 0
    0
    >>> max_subseq(12345, 1)
    5
    """
    "*** YOUR CODE HERE ***"
    if n==0 or l==0 :
        return 0
    last_d=n%10
    t=n//10
    sub1=max_subseq(t,l-1)*10+last_d
    sub2=max_subseq(t,l)
    return max(sub1,sub2)