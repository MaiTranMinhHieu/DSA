def recover_passes(initial, current):
    n = len(initial)
    passes = 0
    temp = list(initial)
    while temp != current and passes < n:
        for j in range(0, n-passes-1):
            if temp[j] > temp[j+1]:
                temp[j], temp[j+1] = temp[j+1], temp[j]
        passes += 1
    return passes

if __name__ == "__main__":
    initial_arr = [5, 1, 4, 2, 8]
    current_arr = [1, 4, 2, 5, 8]
    passes_done = recover_passes(initial_arr, current_arr)
    print(passes_done)