def single_non_duplicate(a):
    l, r = 0, len(a) - 1
    while l < r:
        mid = (l + r) // 2
        if mid % 2 == 1:
            mid -= 1
        if a[mid] == a[mid + 1]:
            l = mid + 2
        else:
            r = mid
    return a[l]

a = [1, 1, 2, 3, 3, 4, 4]
result = single_non_duplicate(a)
print(f"Phần tử đơn lẻ trong mảng đôi là: {result}")