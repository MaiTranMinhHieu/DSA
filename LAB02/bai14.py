def search_matrix(matrix, x):
    if not matrix or not matrix[0]:
        return False
    m, n = len(matrix), len(matrix[0])
    l, r = 0, m * n - 1
    while l <= r:
        mid = (l + r) // 2
        val = matrix[mid // n][mid % n]
        if val == x:
            return True
        elif val < x:
            l = mid + 1
        else:
            r = mid - 1
    return False

matrix = [[1, 3, 5], [7, 9, 11]]
x = 9
result = search_matrix(matrix, x)
print(f"Phần tử x = {x} có tồn tại trong ma trận không? Kết quả: {result}")