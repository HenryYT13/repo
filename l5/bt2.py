a = int(input("Nhập chiều cao 1: "))
b = int(input("Nhập chiều cao 2: "))
c = int(input("Nhập chiều cao 3: "))
if a > b and a > c :
    print(f'Bạn có chiều cao {a} là bạn cao nhất')
elif b > c and b > a :
    print(f'Bạn có chiều cao {b} là bạn cao nhất')
elif c > a and c > b :
    print(f'Bạn có chiều cao {c} là bạn cao nhất')