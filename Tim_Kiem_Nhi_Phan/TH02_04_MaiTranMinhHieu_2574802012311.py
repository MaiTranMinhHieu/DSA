def binary_search(arr, x):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            right = mid - 1
        else:
            left = mid + 1
    return -1

arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]

key_a = 95
result_a = binary_search(arr, key_a)
print(f"a) Kết quả tìm kiếm key x = {key_a}:")
if result_a != -1:
    print(f"   Tìm thấy tại vị trí i = {result_a}")
else:
    print("   Không tìm thấy phần tử trong mảng (-1)")

print("-" * 40)

key_b = 5
result_b = binary_search(arr, key_b)
print(f"b) Kết quả tìm kiếm key x = {key_b}:")
if result_b != -1:
    print(f"   Tìm thấy tại vị trí i = {result_b}")
else:
    print("   Không tìm thấy phần tử trong mảng (-1)")