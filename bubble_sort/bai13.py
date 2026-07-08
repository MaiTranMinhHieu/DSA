def stable_bubble_sort_pairs(a):
    n = len(a)
    for i in range(n):
        for j in range(0, n-i-1):
            if a[j][0] > a[j+1][0]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

if __name__ == "__main__":
    arr = [(2, 'A'), (1, 'B'), (2, 'C'), (1, 'D')]
    result = stable_bubble_sort_pairs(arr)
    print(result)