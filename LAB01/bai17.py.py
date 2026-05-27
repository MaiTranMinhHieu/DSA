def tim_kiem_linh_canh(a, x):
    n = len(a)
    if n == 0:
        return -1
    last = a[n - 1]
    a[n - 1] = x
    i = 0
    while a[i] != x:
        i += 1
    a[n - 1] = last
    if i < n - 1 or a[n - 1] == x:
        return i
    return -1