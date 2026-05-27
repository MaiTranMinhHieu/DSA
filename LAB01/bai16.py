def phan_tu_gan_nhat(a, x):
    if not a:
        return None, -1
    min_diff = abs(a[0] - x)
    val = a[0]
    idx = 0
    for i in range(1, len(a)):
        diff = abs(a[i] - x)
        if diff < min_diff:
            min_diff = diff
            val = a[i]
            idx = i
    return val, idx