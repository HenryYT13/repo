a, b = int(input("Nhập số a: ")), int(input("Nhập số b: "))
m, n = a,b
while n != 0:
    r = m % n
    m = n
    n = r   
ucln = m
bcnn = (a * b) // ucln
print(f"Ước số chung lớn nhất của {a} và {b} là: {bcnn}")
tu = a // ucln
mau = b // ucln
print(f"Tử số: {tu}")
print(f"Mẫu số: {mau}")