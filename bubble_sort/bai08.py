def check_sorted_after_k_passes(a, k):
    n = len(a)
    for i in range(min(k, n)):
        for j in range(0, n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    for i in range(n - 1):
        if a[i] > a[i+1]:
            return False
    return True

if __name__ == "__main__":
    arr = [5, 1, 4, 2, 8]
    k = 2
    is_sorted = check_sorted_after_k_passes(arr, k)
    print(is_sorted)