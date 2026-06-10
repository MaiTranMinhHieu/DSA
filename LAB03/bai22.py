def bubble_sort_deviation_k(a, k):
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(0, min(n-i-1, n-1)):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
        if not swapped:
            break
    return a

if __name__ == "__main__":
    arr = [3, 1, 2, 5, 4]
    k_val = 2
    result = bubble_sort_deviation_k(arr, k_val)
    print(result)