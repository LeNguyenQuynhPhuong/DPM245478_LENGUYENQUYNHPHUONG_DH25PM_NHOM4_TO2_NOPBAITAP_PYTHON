'''Câu 7: Tính và xuất độ dài đoạn AB
Yêu cầu:
Nhập toạ độ 2 điểm A(xA,yA), B(xB,yB). Tính và xuất độ dài đoạn AB. '''
import math

print("Nhap toa do diem A: ")
xa = float(input("xA ="))
ya = float(input("yA="))

print("Nhap toa do diem B: ")
xb = float(input("xB ="))
yb = float(input("yB ="))

d = math.sqrt((xb - xa))**2 + (yb - ya)**2

print("Do dai doan AB =",d)

