'''Câu 9: Nhập vào 1 tháng, xuất ra tháng đó thuộc quý mấy trong năm. '''
month = int(input("Nhập tháng (1-12): "))

if 1 <= month <= 3:
    print("Tháng này thuộc quý 1")
elif 4 <= month <= 6:
    print("Tháng này thuộc quý 2")
elif 7 <= month <= 9:
    print("Tháng này thuộc quý 3")
elif 10 <= month <= 12:
    print("Tháng này thuộc quý 4")
else:
    print("Tháng không hợp lệ")