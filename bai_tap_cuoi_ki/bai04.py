def dem_ngay_am_hon(T):
    n = len(T)
    kq = [0] * n
    stack = []
    
    for i in range(n):
        while stack and T[i] > T[stack[-1]]:
            ngay_truoc = stack.pop()
            kq[ngay_truoc] = i - ngay_truoc
        stack.append(i)
        
    return kq

T = [73, 74, 75, 71, 69, 72, 76, 73]
print("Câu 4 - Số ngày chờ nhiệt độ cao hơn:", dem_ngay_am_hon(T))