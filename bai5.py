import matplotlib.pyplot as plt

sales = {'Laptop': 10, 'Mouse': 50, 'Keyboard': 30}
prices = {'Laptop': 1500, 'Mouse': 20, 'Keyboard': 50}

def tinh_doanh_thu(sales, prices):
    doanh_thu = {}
    tong = 0

    for sp in sales:
        doanh_thu[sp] = sales[sp] * prices[sp]
        tong += doanh_thu[sp]

    return doanh_thu, tong

def ve_bieu_do(sales):
    names = list(sales.keys())
    values = list(sales.values())

    plt.bar(names, values)
    plt.title("Số lượng sản phẩm bán ra")
    plt.xlabel("Sản phẩm")
    plt.ylabel("Số lượng")
    plt.show()

doanh_thu, tong = tinh_doanh_thu(sales, prices)

print("Doanh thu từng sản phẩm:")
print(doanh_thu)
print("Tổng doanh thu:", tong)

ve_bieu_do(sales)