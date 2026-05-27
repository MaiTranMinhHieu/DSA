import math

def check_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def tim_nguyen_to_dau_tien(a):
    for i in range(len(a)):
        if check_prime(a[i]):
            return a[i], i
    return -1, -1