# bai04.py
def search_rotated(a, x):
    l, r = 0, len(a) - 1
    while l <= r:
        m = (l + r) // 2
        if a[m] == x: return m
        if a[l] <= a[m]:
            if a[l] <= x < a[m]: r = m - 1
            else: l = m + 1
        else:
            if a[m] < x <= a[r]: l = m + 1
            else: r = m - 1
    return -1

if __name__ == "__main__":
    a = [4, 5, 6, 7, 0, 1, 2]
    x = 0
    print(f"Chi so cua {x} la: {search_rotated(a, x)}")