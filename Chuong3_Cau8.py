'''Câu 8: Nhập vào 2 giá trị a, b và phép toán ‘+’, ‘-’, ‘*’, ‘/’ . Hãy xuất kết quả theo 
đúng phép toán đã nhập.'''
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
op = input("Nhập phép toán (+, -, *, /): ")

if op == '+':
    print("Kết quả:", a + b)
elif op == '-':
    print("Kết quả:", a - b)
elif op == '*':
    print("Kết quả:", a * b)
elif op == '/':
    if b == 0:
        print("Không thể chia cho 0")
    else:
        print("Kết quả:", a / b)
else:
    print("Phép toán không hợp lệ")