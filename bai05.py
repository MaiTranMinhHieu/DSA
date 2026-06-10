def count_comparisons(a):
    n = len(a)
    comps = 0
    for i in range(n):
        for j in range(0, n-i-1):
            comps += 1
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return comps

if __name__ == "__main__":
    arr = [1, 2, 3]
    total_comps = count_comparisons(arr)
    print(total_comps)