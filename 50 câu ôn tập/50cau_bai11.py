# bai11.py
def selection_sort(a):
    n = len(a)
    so_sanh = 0
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            so_sanh += 1
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return so_sanh

if __name__ == "__main__":
    a = [5, 4, 3, 2, 1]
    n = len(a)
    so_sanh = selection_sort(a)
    ly_thuyet = n * (n - 1) // 2
    print(f"So phep so sanh thuc te: {so_sanh}")
    print(f"So phep so sanh ly thuyet n(n-1)/2: {ly_thuyet}")