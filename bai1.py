def nhap_danh_sach():
    ds = []
    n = int(input("Nhập số lượng món hàng: "))
    for i in range(n):
        ten = input(f"Nhập tên món {i+1}: ")
        gia = float(input(f"Nhập giá tiền {i+1}: "))
        ds.append((ten, gia))
    return ds

def tinh_toan(ds):
    tong = sum(gia for ten, gia in ds)
    max_item = max(ds, key=lambda x: x[1])
    return tong, max_item

def ghi_file(ds, tong, max_item):
    with open("chi_tieu.txt", "w", encoding="utf-8") as f:
        f.write("Danh sách chi tiêu:\n")
        for ten, gia in ds:
            f.write(f"{ten}: {gia}\n")
        f.write(f"\nTổng tiền: {tong}\n")
        f.write(f"Món đắt nhất: {max_item[0]} - {max_item[1]}\n")

ds = nhap_danh_sach()
tong, max_item = tinh_toan(ds)
ghi_file(ds, tong, max_item)