def find_min_rotated(a):
    l, r = 0, len(a) - 1
    while l < r:
        mid = (l + r) // 2
        if a[mid] > a[r]:
            l = mid + 1
        else:
            r = mid
    return a[l]

a = [3, 4, 5, 1, 2]
result = find_min_rotated(a)
print(f"Phần tử nhỏ nhất trong mảng xoay là: {result}")