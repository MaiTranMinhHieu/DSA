def search_insert_position(a, x):
    l, r = 0, len(a) - 1
    ans = len(a)
    while l <= r:
        mid = (l + r) // 2
        if a[mid] >= x:
            ans = mid
            r = mid - 1
        else:
            l = mid + 1
    return ans

a = [1, 3, 5, 6]
x = 4
result = search_insert_position(a, x)
print(f"Vị trí chèn phần tử x = {x} vào mảng là: {result}")