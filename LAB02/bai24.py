def min_max_gas_dist(x, k):
    def check(dist):
        count = 0
        for i in range(len(x) - 1):
            count += int((x[i+1] - x[i]) / dist)
        return count <= k

    l, r = 0.0, float(x[-1] - x[0])
    while r - l > 1e-6:
        mid = (l + r) / 2.0
        if check(mid):
            r = mid
        else:
            l = mid
    return r

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 9
result = min_max_gas_dist(x, k)
print(f"Khoảng cách lớn nhất giữa hai trạm xăng liền kề sau khi thêm k = {k} trạm mới là: {result:.6f}")