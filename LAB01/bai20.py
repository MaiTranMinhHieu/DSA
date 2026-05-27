danh_ba = []

def them_lien_he(ten, sdt):
    danh_ba.append({"ten": ten, "sdt": sdt})

def tim_sdt(ten):
    for lh in danh_ba:
        if lh["ten"] == ten:
            return lh["sdt"]
    return "Khong tim thay"

def tim_ten(sdt):
    for lh in danh_ba:
        if lh["sdt"] == sdt:
            return lh["ten"]
    return "Khong tim thay"

def dem_dau_so(dau_so):
    count = 0
    for lh in danh_ba:
        if lh["sdt"].startswith(dau_so):
            count += 1
    return count

while True:
    chon = input()
    if chon == '1':
        t = input()
        s = input()
        them_lien_he(t, s)
    elif chon == '2':
        t = input()
        print(tim_sdt(t))
    elif chon == '3':
        s = input()
        print(tim_ten(s))
    elif chon == '4':
        ds = input()
        print(dem_dau_so(ds))
    elif chon == '0':
        break