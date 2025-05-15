a = int(input("Nhập số a: "))
for i in range(2, a):
    if a % i == 0:
        print(f"{a} Ko phải là SNT")
        break
else:
    print(f"{a} Là SNT")