def int_sqrt(n):
    if n == 0 or n == 1:
        return n
    l, r = 1, n
    ans = 1
    while l <= r:
        mid = (l + r) // 2
        if mid * mid <= n:
            ans = mid
            l = mid + 1
        else:
            r = mid - 1
    return ans

n1 = 8
result1 = int_sqrt(n1)
print(f"Phần nguyên căn bậc hai của n = {n1} là: {result1}")

n2 = 16
result2 = int_sqrt(n2)
print(f"Phần nguyên căn bậc hai của n = {n2} là: {result2}")