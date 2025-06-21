def is_prime(n):
    k = 2
    while k < n:
        if n % k == 0:
            return False
        k = k + 1
    return True
def nearest_prime(n):
 """Return the nearest prime number to n.
 In a tie, return the larger one.
 >>> nearest_prime(8)
 7
 >>> nearest_prime(11)
 11
 >>> nearest_prime(21)
 23
 """ 
 k=0
 while True: 
    if is_prime(n+k): 
        return n+k
    if k>0:
        k =-k 
    else:
        k=-k+1
