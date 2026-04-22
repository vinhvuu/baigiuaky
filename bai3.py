def c_to_f(c):
    return c * 9/5 + 32

def f_to_c(f):
    return (f - 32) * 5/9

def usd_to_vnd(usd, rate):
    return usd * rate

try:
    c = float(input("Nhập độ C: "))
    print("Độ F:", c_to_f(c))

    f = float(input("Nhập độ F: "))
    print("Độ C:", f_to_c(f))

    usd = float(input("Nhập USD: "))
    rate = float(input("Nhập tỷ giá USD -> VND: "))
    print("VND:", usd_to_vnd(usd, rate))

except ValueError:
    print("Lỗi: Bạn phải nhập số!")