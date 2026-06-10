def last_element_after_one_pass(a):
    for i in range(len(a) - 1):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
    return a[-1]

if __name__ == "__main__":
    arr = [5, 1, 4, 2, 8]
    last_element = last_element_after_one_pass(arr)
    print(last_element)