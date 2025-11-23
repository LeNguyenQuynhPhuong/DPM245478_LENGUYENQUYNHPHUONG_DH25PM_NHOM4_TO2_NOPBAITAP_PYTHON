'''Câu 7: Viết chương trình nhập vào một dãy các số theo thứ  tự tăng, nếu nhập sai 
quy cách thì yêu cầu nhập lại. In dãy số sau khi đã nhập xong '''
def NhapDaySoTangDan():
    day_so = []
    n = int(input("Nhập số lượng phần tử trong dãy số: "))
    print("Nhập các số theo thứ tự tăng dần:")
    for i in range(n):
        while True:
            num = int(input(f"Nhập số thứ {i + 1}: "))
            if i == 0 or num > day_so[i - 1]:
                day_so.append(num)
                break
            else:
                print("Số nhập vào không đúng thứ tự tăng, vui lòng nhập lại.")
    return day_so

result = NhapDaySoTangDan()
print("Dãy số đã nhập theo thứ tự tăng dần là:", result)
