def sort_students_by_score_and_name(a):
    n = len(a)
    for i in range(n):
        for j in range(0, n-i-1):
            if a[j][1] < a[j+1][1] or (a[j][1] == a[j+1][1] and a[j][0] > a[j+1][0]):
                a[j], a[j+1] = a[j+1], a[j]
    return a

if __name__ == "__main__":
    arr = [("An", 8), ("Binh", 9), ("Anh", 8)]
    result = sort_students_by_score_and_name(arr)
    print(result)