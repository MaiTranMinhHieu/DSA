def dem_xuat_hien(a, x):
    count = 0
    for i in range(len(a)):
        if a[i] == x:
            count += 1
    return count