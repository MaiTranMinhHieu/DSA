# bai12.py
def selection_sort_unstable_demo():
    # Mảng gồm các tuple (giá trị, id nhận diện)
    # Hai phần tử có giá trị 2 là (2, 'A') xuất hiện trước (2, 'B')
    a = [(2, 'A'), (2, 'B'), (1, 'C')]
    n = len(a)
    print("Truoc khi sap xep:", a)
    
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j][0] < a[min_idx][0]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
        
    print("Sau khi sap xep:  ", a)
    print("Giai thich: (1, 'C') doi cho voi (2, 'A'), lam cho (2, 'A') bi day ra sau (2, 'B'). Tinh on dinh bi pha vỡ.")

if __name__ == "__main__":
    selection_sort_unstable_demo()