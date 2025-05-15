a = int(input("Nhap canh 1: "))
b = int(input("Nhap canh 2: "))
c = int(input("Nhap canh 3: "))
if (a+b) > c:{
    print("Tam giac la tam giac that")
}
elif (a+c) > b:{
    print("Tam giac la tam giac that")
}
elif (b+c) > a:{
    print("Tam giac la tam giac that")
}
else:{
    print("Tam giac khong la tam giac that")
}