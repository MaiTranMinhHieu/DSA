# bai10.py
def binary_insertion_sort(a):
    shifts = 0
    for i in range(1, len(a)):
        key = a[i]
        l, r = 0, i - 1
        while l <= r:
            m = (l + r) // 2
            if a[m] < key: l = m + 1
            else: r = m - 1
        
        for j in range(i - 1, l - 1, -1):
            a[j + 1] = a[j]
            shifts += 1
        a[l] = key
    return shifts

if __name__ == "__main__":
    a = [3, 2, 1]
    shifts = binary_insertion_sort(a)
    print(f"So shift giu nguyen: {shifts}")