# bai05.py
import math

def min_eating_speed(pile, h):
    l, r = 1, max(pile)
    res = r
    while l <= r:
        m = (l + r) // 2
        hours = sum(math.ceil(p / m) for p in pile)
        if hours <= h:
            res, r = m, m - 1
        else:
            l = m + 1
    return res

if __name__ == "__main__":
    pile = [3, 6, 7, 11]
    h = 8
    print(f"Toc do an nho nhat: {min_eating_speed(pile, h)}")