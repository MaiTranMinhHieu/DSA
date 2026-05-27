def tim_tat_ca(a, x):
    result = []
    for i in range(len(a)):
        if a[i] == x:
            result.append(i)
    return result