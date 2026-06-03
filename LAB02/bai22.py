def find_median_sorted_arrays(a, b):
    if len(a) > len(b):
        a, b = b, a
    m, n = len(a), len(b)
    l, r = 0, m
    while l <= r:
        part_a = (l + r) // 2
        part_b = (m + n + 1) // 2 - part_a
        
        max_left_a = float('-inf') if part_a == 0 else a[part_a - 1]
        min_right_a = float('inf') if part_a == m else a[part_a]
        max_left_b = float('-inf') if part_b == 0 else b[part_b - 1]
        min_right_b = float('inf') if part_b == n else b[part_b]
        
        if max_left_a <= min_right_b and max_left_b <= min_right_a:
            if (m + n) % 2 == 0:
                return (max(max_left_a, max_left_b) + min(min_right_a, min_right_b)) / 2.0
            else:
                return max(max_left_a, max_left_b)
        elif max_left_a > min_right_b:
            r = part_a - 1
        else:
            l = part_a + 1

a1 = [1, 3]
b1 = [2]
result1 = find_median_sorted_arrays(a1, b1)
print(f"Trung vị của hai mảng {a1} và {b1} là: {result1}")

a2 = [1, 2]
b2 = [3, 4]
result2 = find_median_sorted_arrays(a2, b2)
print(f"Trung vị của hai mảng {a2} và {b2} là: {result2}")