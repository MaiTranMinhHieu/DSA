# bai07.py
def bubble_sort(a):
    n = len(a)
    swaps = 0
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1
    return swaps

if __name__ == "__main__":
    a = [2, 3, 1]
    swaps = bubble_sort(a)
    print(f"So swap: {swaps}")