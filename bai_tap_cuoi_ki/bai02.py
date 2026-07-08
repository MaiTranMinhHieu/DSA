def dem_dich_chuyen_insertion_sort(A):
    arr = A.copy()
    so_lan_dich = 0
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            so_lan_dich += 1
            j -= 1
        arr[j + 1] = key
        
    return so_lan_dich, arr

A = [5, 2, 4, 6, 1, 3]
so_lan, mang_da_sap_xep = dem_dich_chuyen_insertion_sort(A)
print("Câu 2 - Số lần dịch (số nghịch thế):", so_lan)
print("Câu 2 - Mảng sau khi sắp xếp:", mang_da_sap_xep)