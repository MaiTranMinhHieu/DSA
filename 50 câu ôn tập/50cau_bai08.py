# bai08.py
def optimized_bubble_sort(a):
    n = len(a)
    luot = 0
    for i in range(n):
        luot += 1
        swapped = False
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return luot

if __name__ == "__main__":
    a = [1, 2, 3, 4]
    luot = optimized_bubble_sort(a)
    print(f"So luot: {luot}")