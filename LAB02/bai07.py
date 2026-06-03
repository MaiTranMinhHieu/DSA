def upper_bound(a, x):
    l, r = 0, len(a) - 1
    ans = len(a)
    while l <= r:
        mid = (l + r) // 2
        if a[mid] > x:
            ans = mid
            r = mid - 1
        else:
            l = mid + 1
    return ans

a = [1, 3, 5, 7]
x = 5
result = upper_bound(a, x)
print(f"Chỉ số của phần tử nhỏ nhất > {x} (Upper Bound) là: {result}")