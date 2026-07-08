def cocktail_shaker_sort(a):
    n = len(a)
    swapped = True
    start = 0
    end = n - 1
    while swapped:
        swapped = False
        for i in range(start, end):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True
        if not swapped:
            break
        swapped = False
        end -= 1
        for i in range(end - 1, start - 1, -1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True
        start += 1
    return a

if __name__ == "__main__":
    arr = [5, 1, 4, 2, 8]
    result = cocktail_shaker_sort(arr)
    print(result)