# toan = int(input("Nhập điểm toán: "))
# anh = int(input("Nhập điểm anh: "))
# tin = int(input("Nhập điểm tin: "))

# tb = (toan + anh + tin) / 3

# if tb >= 8:
#     print("Giỏi")
# elif tb >= 6.5:
#     print("Khá")
# elif tb >= 5:
#     print("Trung bình")
# else:
#     print("Yếu")

# print("Bảng cửu chương 9")
# for i in range(1, 11):
#     print(f"9 x {i} = {9 * i}")


# n = int(input("Nhập n: "))
# while n == -1:
#     print("Nhập lại n")
#     n = int(input("Nhập n: "))

# # for i in range(n, 101, 1):
# #     print(i)
# while n < 100:
#     print(n)
#     n = n + 1

# if n > 100:
#     exit()

import random
import os
os.system("cls")
n = random.randint(1, 100)
a = int(input("Nhập số mà bạn nghĩ là đúng: "))
while a != n:
    if a < n:
        os.system("cls")
        print(f"Nhập số lớn hơn {a} (số bí ẩn lớn hơn số bạn nhập)")
    else:
        os.system("cls")
        print(f"Nhập số nhỏ hơn {a} (số bí ẩn nhỏ hơn số bạn nhập)")
    a = int(input("Vui lòng nhập lại số bạn nghĩ là đúng: "))
print(f"Chính xác, số bí ẩn là: {n}")
