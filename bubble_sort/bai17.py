def partial_bubble_sort(a, k):
    n = len(a)
    for i in range(min(k, n)):
        for j in range(0, n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

if __name__ == "__main__":
    arr = [5, 1, 4, 2, 8]
    k = 2
    result = partial_bubble_sort(arr, k)
    print(result)