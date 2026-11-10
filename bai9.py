ds=[]
def nhapds():
    n=int(input("nhap so sinh vien:"))
    for i in range(n):
        masv = input("nhap ma sv:")
        ten = input("nhap ten:")
        gioitinh = input("nhap gioi tinh:")
        tuoi = int(input("nhap tuoi:"))
        toan = float(input("nhap diem toan:"))
        ly = float(input("nhap diem ly:"))
        hoa = float(input("nhap diem hoa:"))
        # tinh diem tb
        dtb = toan + ly + hoa / 3
        # hoc luc
        if dtb >= 8:
            xeploai = "gioi"
        elif dtb >= 6.5:
            xeploai = "kha"
        elif dtb >= 5:
            xeploai = "trung binh"
        else:
            xeploai = "yeu"
        sv = {"masv":masv,"ten": ten,"gioi tinh":gioitinh,"tuoi": tuoi,
        "toan":toan,"ly": ly,"hoa": hoa,"dtb": dtb,"xep loai": xeploai}
        ds.append(sv)

def inds():
    print("danh sach sinh vien:")
    for sv in ds:
       print(sv.get("masv"),"-",sv.get("ten"),"-",sv.get("gioi tinh"),"-",
             sv.get("tuoi"),"-",sv.get("toan"),"-",sv.get("ly"),"-",sv.get("hoa"),"-",
             sv.get("xep loai"),"-",sv.get("dtb"))

def themsv(ds):
    print("nhap thong tin sinh vien can them:")
    masv = input("nhap ma sv:")
    ten = input("nhap ten:")
    gioitinh = input("nhap gioi tinh:")
    tuoi = int(input("nhap tuoi:"))
    toan = float(input("nhap diem toan:"))
    ly = float(input("nhap diem ly:"))
    hoa = float(input("nhap diem hoa:"))
    # tinh diem tb
    dtb = toan + ly + hoa / 3
    # hoc luc
    if dtb >= 8:
        xeploai= "gioi"
    elif dtb >= 6.5:
        xeploai= "kha"
    elif dtb >= 5:
        xeploai = "trung binh"
    else:
        xeploai = "yeu"
    sv = {"masv": masv, "ten": ten, "gioi tinh": gioitinh, "tuoi": tuoi,
          "toan": toan, "ly": ly, "hoa": hoa, "dtb": dtb, "xep loai": xeploai}
    ds.append(sv)

def capnhat(masv):
    for sv in ds:
        if sv["masv"] == masv:
          ten=input("nhap ten:")
          gioitinh = input("nhap gioi tinh:")
          tuoi = int(input("nhap tuoi:"))
          toan = float(input("nhap diem toan:"))
          ly = float(input("nhap diem ly:"))
          hoa = float(input("nhap diem hoa:"))
          dtb=toan+ly+hoa/3
          if dtb >= 8:
             xeploai = "gioi"
          elif dtb >= 6.5:
             xeploai = "kha"
          elif dtb >= 5:
             xeploai = "trung binh"
          else:
             xeploai = "yeu"
          sv["ten"]=ten
          sv["gioi tinh"]=gioitinh
          sv["tuoi"] = tuoi
          sv["toan"] = ten
          sv["ly"] = ly
          sv["hoa"] = hoa
          sv["dtb"] = dtb
          sv["xep loai"] = xeploai

def xoasv(masvxoa):
    for sv in ds:
        if sv["ma sv"] == masvxoa:
            ds.remove(sv)

def timkiem(dsten):
    for sv in ds:
        if sv["ten"] == dsten:
            return "co sinh vien"
    return "khong co sinh vien"
def sapxepdtb(dtb):
    ds.sort(key=lambda sv:sv["dtb"])
    for sv in ds:
        print(sv)

def sapxepten(ten):
    ds.sort(key=lambda sv: sv["ten"])
    for sv in ds:
        print(sv)

def sapxepmasv(masv):
    ds.sort(key=lambda sv: sv["masv"])
    for sv in ds:
        print(sv)

sosv=int(input("so luong sinh vien:"))
nhapds()
print("danh sach sinh vien vua nhap:")
inds()

masvxoa=input("nhap so sinh vien sau khi xoa:")
print(xoasv(masvxoa))

dsten=input("nhap ten sinh vien can tim:")
print(timkiem(dsten))

dtb=input("nhap diem trung binh cua sinh vien:")
print(sapxepdtb(dtb))

ten=input("nhap ten sinh vien sau khi sap xep:")
print(sapxepten(ten))

masv=input("nhap ma sinh vien sau khi sap xep:")
print(sapxepmasv(masv)) 








