a = int(input("Nhập số nguyên A : "))
b = int(input("Nhập số nguyên B : "))
sum = 0
if a % 2 != 0 :
    a = a + 1
for i in range (a ,b ,2) :
    sum = sum + i
print(sum)