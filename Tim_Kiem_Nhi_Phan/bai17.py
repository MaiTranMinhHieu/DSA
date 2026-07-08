def ship_within_days(weights, days):
    def can_ship(capacity):
        d, current_load = 1, 0
        for w in weights:
            if current_load + w > capacity:
                d += 1
                current_load = 0
            current_load += w
        return d <= days

    l, r = max(weights), sum(weights)
    ans = r
    while l <= r:
        mid = (l + r) // 2
        if can_ship(mid):
            ans = mid
            r = mid - 1
        else:
            l = mid + 1
    return ans

weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
days = 5
result = ship_within_days(weights, days)
print(f"Sức chứa tàu nhỏ nhất để chở hết hàng trong {days} ngày là: {result}")