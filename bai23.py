def profile_bubble_sort(a):
    n = len(a)
    comps = 0
    swaps = 0
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            comps += 1
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swaps += 1
                swapped = True
        if not swapped:
            break
    return comps, swaps

if __name__ == "__main__":
    arr = [5, 1, 4, 2, 8]
    total_comps, total_swaps = profile_bubble_sort(arr)
    print(total_comps, total_swaps)