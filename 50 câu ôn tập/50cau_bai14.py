# bai14.py
def shell_sort(a, gaps):
    shifts = 0
    n = len(a)
    for gap in gaps:
        for i in range(gap, n):
            temp = a[i]
            j = i
            while j >= gap and a[j - gap] > temp:
                a[j] = a[j - gap]
                shifts += 1
                j -= gap
            a[j] = temp
    return shifts

if __name__ == "__main__":
    a = [9, 8, 3, 7, 5, 6, 4, 1]
    gaps = [4, 2, 1]
    shifts = shell_sort(a, gaps)
    print(f"Mang sau khi xep: {a}")
    print(f"So shift voi gap {gaps}: {shifts}")