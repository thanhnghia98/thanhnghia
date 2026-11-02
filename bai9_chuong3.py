ds=[]
n= int(input("nhap so sinh vien:"))
# nhap ds
for i in range(n):
    sv={}
    sv["ma sv"]=input("nhap ma sv:")
    sv["ten"]=input("nhap ten:")
    sv["gioi tinh"]=input("nhap gioi tinh:")
    sv["tuoi"]=int(input("nhap tuoi:"))
    sv["toan"]=float(input("nhap diem toan:"))
    sv["ly"]=float(input("nhap diem ly:"))
    sv["hoa"]=float(input("nhap diem hoa:"))
# tinh diem tb
    sv["dtb"] = (sv["toan"]+sv["ly"]+sv["hoa"])/3
# hoc luc
    if sv["dtb"] >= 8:
     sv["hoc luc"] = "gioi"
    elif sv["dtb"] >= 6.5:
     sv["hoc luc"] = "kha"
    elif sv["dtb"] >= 5:
     sv["hoc luc"] = "trung binh"
    else:
     sv["hoc luc"] = "yeu"
    ds.append(sv)
print(ds)

def themsv(ds):
    sv = {}
    sv["ma sv"] = input("nhap ma sv:")
    sv["ten"] = input("nhap ten:")
    sv["gioi tinh"] = input("nhap gioi tinh:")
    sv["tuoi"] = int(input("nhap tuoi:"))
    sv["toan"] = float(input("nhap diem toan:"))
    sv["ly"] = float(input("nhap diem ly:"))
    sv["hoa"] = float(input("nhap diem hoa:"))
    # tinh diem tb
    sv["dtb"] = (sv["toan"] + sv["ly"] + sv["hoa"]) / 3
    # hoc luc
    if sv["dtb"] >= 8:
        sv["hoc luc"] = "gioi"
    elif sv["dtb"] >= 6.5:
        sv["hoc luc"] = "kha"
    elif sv["dtb"] >= 5:
        sv["hoc luc"] = "trung binh"
    else:
        sv["hoc luc"] = "yeu"
    ds.append(sv)
def capnhat(ds,masv):
    sv = {}
    sv["ma sv"] = input("nhap ma sv:")
    sv["ten"] = input("nhap ten:")
    sv["gioi tinh"] = input("nhap gioi tinh:")
    sv["tuoi"] = int(input("nhap tuoi:"))
    sv["toan"] = float(input("nhap diem toan:"))
    sv["ly"] = float(input("nhap diem ly:"))
    sv["hoa"] = float(input("nhap diem hoa:"))
def xoasv(ds,masv):
    for sv in ds:
        if sv["ma sv"] == masv:
            ds.remove(sv)
            print("xoa thanh cong:")
            return
def timkiem(ds,ten):
    for sv in ds:
        if sv["ten"] == ten:
            print(sv)
            return
def sapxep(ds):
    ds.sort(key=lambda sv: sv["dtb"])
    for sv in ds:
        print(sv)
def sapxepten(ds,ten):
    ds.sort(key=lambda sv: sv["ten"])
    for sv in ds:
        print(sv)
def sapxepmasv(ds,masv):
    ds.sort(key=lambda sv: sv["masv"])
    for sv in ds:
        print(sv)
def inds(ds):
    for sv in ds:
        print("ma sv:",sv["ma"])
        print("ten:",sv["ten"])
        print("gioi tinh:",sv["gioi"])
        print("tuoi:",sv["tuoi"])
        print("diem hoa:",sv["hoa"])
        print("dtb:",sv["dtb"])
        print("diem ly:",sv["ly"])
        print("hoa luc:",sv["hoc"])
        print("diem toan:",sv["toan"])
        print("_________")