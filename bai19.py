def min_passes_nearly_sorted(a):
    n = len(a)
    passes = 0
    for i in range(n):
        swapped = False
        passes += 1
        for j in range(0, n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
        if not swapped:
            break
    return passes

if __name__ == "__main__":
    arr = [1, 2, 4, 3, 5]
    passes = min_passes_nearly_sorted(arr)
    print(passes)