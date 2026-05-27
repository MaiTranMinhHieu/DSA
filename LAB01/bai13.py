def tim_chuoi(ds, ten):
    ten_thuong = ten.lower()
    for i in range(len(ds)):
        if ds[i].lower() == ten_thuong:
            return i
    return -1