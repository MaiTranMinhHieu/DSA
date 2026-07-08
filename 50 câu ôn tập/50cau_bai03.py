# bai03.py
def lower_bound(a, x):
    l, r, res = 0, len(a) - 1, len(a)
    while l <= r:
        m = (l + r) // 2
        if a[m] >= x:
            res, r = m, m - 1
        else:
            l = m + 1
    return res

def upper_bound(a, x):
    l, r, res = 0, len(a) - 1, len(a)
    while l <= r:
        m = (l + r) // 2
        if a[m] > x:
            res, r = m, m - 1
        else:
            l = m + 1
    return res

if __name__ == "__main__":
    a = [1, 3, 5, 7]
    x = 4
    print(f"lower={lower_bound(a, x)}")