def tuyen_tinh(array, n, x):
    for i in range(0, n):
        if (array[i] == x):
            return i
    return -1
array = [15, 25, 80, 30, 60, 50,110, 100, 130, 180]
x = 110
arr = [15, 25, 80, 30, 60, 50, 110, 100, 130, 180]
y = 185;
n = len(array)
result = tuyen_tinh(array, n, x)
res = tuyen_tinh(arr,n,y)
print(f"array:{array}")
print(f"x={x}")
print("Phan tu tim thay duoc tai vi tri la:", result)
print("-----------------------------------")
print(f"array:{arr}")
print(f"x={y}")
print(res)
print("Phan tu khong duoc tim thay trong arr[]")