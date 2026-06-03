def split_array(a, k):
    def is_valid(max_sum):
        splits, current_sum = 1, 0
        for num in a:
            if current_sum + num > max_sum:
                splits += 1
                current_sum = num
                if splits > k:
                    return False
            else:
                current_sum += num
        return True

    l, r = max(a), sum(a)
    ans = r
    while l <= r:
        mid = (l + r) // 2
        if is_valid(mid):
            ans = mid
            r = mid - 1
        else:
            l = mid + 1
    return ans

a = [7, 2, 5, 10, 8]
k = 2
result = split_array(a, k)
print(f"Tổng lớn nhất trong các đoạn nhỏ nhất khi chia mảng thành {k} đoạn là: {result}")