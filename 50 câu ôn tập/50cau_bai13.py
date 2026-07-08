# bai13.py
def count_inversions(a):
    def merge_sort(arr, temp_arr, left, right):
        inv_count = 0
        if left < right:
            mid = (left + right) // 2
            inv_count += merge_sort(arr, temp_arr, left, mid)
            inv_count += merge_sort(arr, temp_arr, mid + 1, right)
            inv_count += merge(arr, temp_arr, left, mid, right)
        return inv_count

    def merge(arr, temp_arr, left, mid, right):
        i, j, k = left, mid + 1, left
        inv_count = 0
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp_arr[k] = arr[i]
                i += 1
            else:
                temp_arr[k] = arr[j]
                inv_count += (mid - i + 1)
                j += 1
            k += 1
        while i <= mid:
            temp_arr[k] = arr[i]
            i += 1
            k += 1
        while j <= right:
            temp_arr[k] = arr[j]
            j += 1
            k += 1
        for loop_var in range(left, right + 1):
            arr[loop_var] = temp_arr[loop_var]
        return inv_count

    n = len(a)
    temp_arr = [0] * n
    return merge_sort(a, temp_arr, 0, n - 1)

if __name__ == "__main__":
    a = [2, 4, 1, 3, 5]
    print(f"So nghich the (O(n log n)): {count_inversions(a)}")