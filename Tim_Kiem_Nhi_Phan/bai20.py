def allocate_books(p, m):
    if m > len(p):
        return -1
        
    def is_valid(max_pages):
        students, current_pages = 1, 0
        for pages in p:
            if current_pages + pages > max_pages:
                students += 1
                current_pages = pages
                if students > m:
                    return False
            else:
                current_pages += pages
        return True

    l, r = max(p), sum(p)
    ans = r
    while l <= r:
        mid = (l + r) // 2
        if is_valid(mid):
            ans = mid
            r = mid - 1
        else:
            l = mid + 1
    return ans

p = [12, 34, 67, 90]
m = 2
result = allocate_books(p, m)
print(f"Số trang tối đa của một học sinh nhỏ nhất khi chia cho {m} em là: {result}")