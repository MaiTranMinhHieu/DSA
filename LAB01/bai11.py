def tim_max(a):
    if not a:
        return None, -1
    max_val = a[0]
    max_idx = 0
    for i in range(1, len(a)):
        if a[i] > max_val:
            max_val = a[i]
            max_idx = i
    return max_val, max_idx