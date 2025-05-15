toan = float(input("Vui lòng nhập điểm toán: "))
van = float(input("Vui lòng nhập điểm văn: "))
anh = float(input("Vui lòng nhập điểm anh: "))
avg_trung_binh = ( toan + anh + van) // 3
if avg_trung_binh == 8 or avg_trung_binh > 8 :{
    print("Bạn là học sinh giỏi.")
}
elif avg_trung_binh >= 6.5 and avg_trung_binh < 8:{
    print("Bạn là học sinh khá.")
}
elif avg_trung_binh >= 5 and avg_trung_binh < 6.5:{
    print("Bạn là học sinh TB.")
}
else :{
    print("Bạn là học sinh yếu.")
}