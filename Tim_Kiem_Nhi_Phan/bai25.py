def max_distance(x, m):
    x.sort()
    def can_place(dist):
        count, last_pos = 1, x[0]
        for i in range(1, len(x)):
            if x[i] - last_pos >= dist:
                count += 1
                last_pos = x[i]
        return count >= m

    l, r = 1, x[-1] - x[0]
    ans = 1
    while l <= r:
        mid = (l + r) // 2
        if can_place(mid):
            ans = mid
            l = mid + 1
        else:
            r = mid - 1
    return ans

x = [1, 2, 3, 4, 7]
m = 3
result = max_distance(x, m)
print(f"Lực từ nhỏ nhất lớn nhất khi đặt m = {m} nam châm là: {result}")