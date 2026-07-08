def bubble_sort_abs(a):
    n = len(a)
    for i in range(n):
        for j in range(0, n-i-1):
            if abs(a[j]) > abs(a[j+1]):
                a[j], a[j+1] = a[j+1], a[j]
    return a

if __name__ == "__main__":
    arr = [-5, 2, -1, 3, -8]
    result = bubble_sort_abs(arr)
    print(result)