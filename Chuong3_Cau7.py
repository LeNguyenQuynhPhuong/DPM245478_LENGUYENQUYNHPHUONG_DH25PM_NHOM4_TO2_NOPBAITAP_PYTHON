'''Câu 7: Nhập vào một ngày (ngày, tháng, năm). Tìm ngày kế sau ngày  
vừa nhập (ngày/tháng/năm). '''
day = int(input("Nhập ngày: "))
month = int(input("Nhập tháng: "))
year = int(input("Nhập năm: "))

# Kiểm tra năm nhuận
leap = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

# Số ngày trong từng tháng
days_in_month = [31, 29 if leap else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day += 1
if day > days_in_month[month - 1]:
    day = 1
    month += 1
    if month > 12:
        month = 1
        year += 1

print("Ngày kế tiếp là: {}/{}/{}".format(day, month, year))