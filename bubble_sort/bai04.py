def count_swaps(a):
    n = len(a)
    swaps = 0
    for i in range(n):
        for j in range(0, n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swaps += 1
    return swaps

if __name__ == "__main__":
    arr = [3, 2, 1]
    total_swaps = count_swaps(arr)
    print(total_swaps)