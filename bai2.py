def chuan_hoa_ten(ten):
    ten = ten.strip().lower()
    words = ten.split()
    return " ".join(word.capitalize() for word in words)

def sap_xep_theo_ten(ds):
    return sorted(ds, key=lambda x: x.split()[-1])

ds = [" nguYen vaN a ", "tRAn tHi b", " le  van   c "]

ds_chuan = [chuan_hoa_ten(x) for x in ds]
ds_sap_xep = sap_xep_theo_ten(ds_chuan)

print("Danh sách sau chuẩn hóa:")
print(ds_chuan)

print("\nDanh sách sau sắp xếp:")
print(ds_sap_xep)