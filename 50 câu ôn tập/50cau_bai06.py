# bai06.py
def split_array(a, k):
    l, r = max(a), sum(a)
    res = r
    while l <= r:
        m = (l + r) // 2
        partitions, current_sum = 1, 0
        for num in a:
            if current_sum + num > m:
                partitions += 1
                current_sum = num
            else:
                current_sum += num
        if partitions <= k:
            res, r = m, m - 1
        else:
            l = m + 1
    return res

if __name__ == "__main__":
    a = [7, 2, 5, 10, 8]
    k = 2
    print(f"Tong lon nhat nho nhat: {split_array(a, k)}")