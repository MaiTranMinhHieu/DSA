# bai09.py
def insertion_sort(a):
    shifts = 0
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            shifts += 1
            j -= 1
        a[j + 1] = key
    return shifts

if __name__ == "__main__":
    a = [3, 2, 1]
    shifts = insertion_sort(a)
    print(f"So shift: {shifts}")