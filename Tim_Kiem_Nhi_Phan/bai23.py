def kth_smallest_matrix(matrix, k):
    n = len(matrix)
    def count_less_equal(mid):
        count, row, col = 0, n - 1, 0
        while row >= 0 and col < n:
            if matrix[row][col] <= mid:
                count += row + 1
                col += 1
            else:
                row -= 1
        return count

    l, r = matrix[0][0], matrix[n - 1][n - 1]
    ans = l
    while l <= r:
        mid = (l + r) // 2
        if count_less_equal(mid) >= k:
            ans = mid
            r = mid - 1
        else:
            l = mid + 1
    return ans

matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
k = 8
result = kth_smallest_matrix(matrix, k)
print(f"Phần tử nhỏ thứ k = {k} trong ma trận là: {result}")