def count_inversions(a):
    n = len(a)
    inversions = 0
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] > a[j]:
                inversions += 1
    return inversions

if __name__ == "__main__":
    arr = [5, 1, 4, 2, 8]
    total_inversions = count_inversions(arr)
    print(total_inversions)