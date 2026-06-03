def count_occurrences(a, x):
    def first_pos(a, x):
        l, r, ans = 0, len(a) - 1, -1
        while l <= r:
            mid = (l + r) // 2
            if a[mid] == x:
                ans, r = mid, mid - 1
            elif a[mid] < x:
                l = mid + 1
            else:
                r = mid - 1
        return ans

    def last_pos(a, x):
        l, r, ans = 0, len(a) - 1, -1
        while l <= r:
            mid = (l + r) // 2
            if a[mid] == x:
                ans, l = mid, mid + 1
            elif a[mid] < x:
                l = mid + 1
            else:
                r = mid - 1
        return ans

    f, l = first_pos(a, x), last_pos(a, x)
    if f == -1:
        return 0
    return l - f + 1

a = [1, 2, 2, 2, 3]
x = 2
result = count_occurrences(a, x)
print(f"Số lần phần tử x = {x} xuất hiện trong mảng là: {result}")