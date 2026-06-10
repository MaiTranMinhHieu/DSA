def count_required_passes(a):
    n = len(a)
    passes = 0
    for i in range(n):
        passes += 1
        swapped = False
        for j in range(0, n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
        if not swapped:
            break
    return passes

if __name__ == "__main__":
    arr = [5, 1, 4, 2, 8]
    passes_needed = count_required_passes(arr)
    print(passes_needed)