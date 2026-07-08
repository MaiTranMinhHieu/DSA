# bai02.py
def find_first_last(a, x):
    def search(is_first):
        l, r, res = 0, len(a) - 1, -1
        while l <= r:
            m = (l + r) // 2
            if a[m] == x:
                res = m
                if is_first: r = m - 1
                else: l = m + 1
            elif a[m] < x:
                l = m + 1
            else:
                r = m - 1
        return res

    dau = search(True)
    cuoi = search(False)
    dem = cuoi - dau + 1 if dau != -1 else 0
    return dau, cuoi, dem

if __name__ == "__main__":
    a = [1, 2, 2, 2, 3]
    x = 2
    dau, cuoi, dem = find_first_last(a, x)
    print(f"dau={dau}, cuoi={cuoi}, dem={dem}")