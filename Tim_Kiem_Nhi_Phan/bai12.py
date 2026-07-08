def find_peak(a):
    l, r = 0, len(a) - 1
    while l < r:
        mid = (l + r) // 2
        if a[mid] > a[mid + 1]:
            r = mid
        else:
            l = mid + 1
    return l

a = [1, 2, 3, 1]
result = find_peak(a)
print(f"Chỉ số của một phần tử đỉnh trong mảng là: {result}")