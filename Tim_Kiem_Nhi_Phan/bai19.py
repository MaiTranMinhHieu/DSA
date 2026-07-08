def aggressive_cows(x, c):
    x.sort()
    def can_place(dist):
        count, last_pos = 1, x[0]
        for i in range(1, len(x)):
            if x[i] - last_pos >= dist:
                count += 1
                last_pos = x[i]
        return count >= c

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

x = [1, 2, 4, 8, 9]
c = 3
result = aggressive_cows(x, c)
print(f"Khoảng cách nhỏ nhất lớn nhất để sắp xếp {c} con bò là: {result}")