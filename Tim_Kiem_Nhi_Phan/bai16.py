def min_eating_speed(piles, h):
    def can_eat(speed):
        hours = 0
        for p in piles:
            hours += (p + speed - 1) // speed
        return hours <= h
    
    l, r = 1, max(piles)
    ans = r
    while l <= r:
        mid = (l + r) // 2
        if can_eat(mid):
            ans = mid
            r = mid - 1
        else:
            l = mid + 1
    return ans

piles = [3, 6, 7, 11]
h = 8
result = min_eating_speed(piles, h)
print(f"Tốc độ ăn nhỏ nhất để Koko ăn hết chuối trong {h} giờ là: {result}")