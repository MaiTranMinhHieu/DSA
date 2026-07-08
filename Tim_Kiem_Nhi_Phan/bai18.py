def find_kth_positive(a, k):
    l, r = 0, len(a) - 1
    while l <= r:
        mid = (l + r) // 2
        missing = a[mid] - mid - 1
        if missing < k:
            l = mid + 1
        else:
            r = mid - 1
    return l + k

a = [2, 3, 4, 7, 11]
k = 5
result = find_kth_positive(a, k)
print(f"Số nguyên dương thứ {k} bị thiếu trong mảng là: {result}")