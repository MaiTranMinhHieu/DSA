class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def tim_dau_chu_trinh(head):
    rua = tho = head
    co_chu_trinh = False
    
    while tho and tho.next:
        rua = rua.next
        tho = tho.next.next
        if rua == tho:
            co_chu_trinh = True
            break
            
    if not co_chu_trinh:
        return None
        
    rua = head
    while rua != tho:
        rua = rua.next
        tho = tho.next
        
    return rua

n1, n2, n3, n4, n5 = Node(1), Node(2), Node(3), Node(4), Node(5)
n1.next, n2.next, n3.next, n4.next = n2, n3, n4, n5
n5.next = n3

nut_chu_trinh = tim_dau_chu_trinh(n1)
print("Câu 6 - Giá trị nút bắt đầu chu trình:", nut_chu_trinh.val if nut_chu_trinh else "Không có")