def find_closest_elements(a, k, x):
    l, r = 0, len(a) - k
    while l < r:
        mid = (l + r) // 2
        if x - a[mid] > a[mid + k] - x:
            l = mid + 1
        else:
            r = mid
    return a[l:l + k]

a = [1, 2, 3, 4, 5]
k = 4
x = 3
result = find_closest_elements(a, k, x)
print(f"Danh sách {k} phần tử gần giá trị x = {x} nhất là: {result}")