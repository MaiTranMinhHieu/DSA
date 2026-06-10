def count_swaps_fast(a):
    def merge_sort_count(arr, temp, left, right):
        inv_count = 0
        if left < right:
            mid = (left + right) // 2
            inv_count += merge_sort_count(arr, temp, left, mid)
            inv_count += merge_sort_count(arr, temp, mid + 1, right)
            inv_count += merge(arr, temp, left, mid, right)
        return inv_count

    def merge(arr, temp, left, mid, right):
        i, j, k, inv_count = left, mid + 1, left, 0
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp[k] = arr[i]
                i += 1
            else:
                temp[k] = arr[j]
                inv_count += (mid - i + 1)
                j += 1
            k += 1
        while i <= mid:
            temp[k] = arr[i]
            i += 1
            k += 1
        while j <= right:
            temp[k] = arr[j]
            j += 1
            k += 1
        for loop_var in range(left, right + 1):
            arr[loop_var] = temp[loop_var]
        return inv_count

    temp_arr = [0] * len(a)
    return merge_sort_count(a, temp_arr, 0, len(a) - 1)

if __name__ == "__main__":
    arr = [5, 1, 4, 2, 8]
    swaps_count = count_swaps_fast(arr)
    print(swaps_count)