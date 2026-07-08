def bubble_sort_one_pass(a):
    for i in range(len(a) - 1):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
    return a

if __name__ == "__main__":
    arr = [5, 1, 4, 2, 8]
    result = bubble_sort_one_pass(arr)
    print(result)