from collections import deque

def min_cua_so_truot(A, k):
    q = deque()
    kq = []
    
    for i in range(len(A)):
        if q and q[0] < i - k + 1:
            q.popleft()
            
        while q and A[q[-1]] >= A[i]:
            q.pop()
            
        q.append(i)
        
        if i >= k - 1:
            kq.append(A[q[0]])
            
    return kq

A = [4, 2, 12, 11, -5, 8, 1, 5, 6]
k = 3
print("Câu 5 - Min của từng cửa sổ trượt:", min_cua_so_truot(A, k))