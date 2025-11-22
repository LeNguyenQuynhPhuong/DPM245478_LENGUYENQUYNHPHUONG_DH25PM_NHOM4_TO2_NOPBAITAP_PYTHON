'''Câu 5: Xử lý chuỗi với các hàm cơ bản
Yêu cầu:
Viết chương trình cho phép nhập vào 1 chuỗi. Yêu cầu xuất ra:
- Bao nhiêu chữ IN HOA
- Bao nhiêu chữ in thường
- Bao nhiêu chữ là chữ số
- Bao nhiêu chữ là ký tự đặc biệt
- Bao nhiêu chữ là khoảng trắng
- Bao nhiêu chữ là Nguyên Âm
- Bao nhiêu chữ là Phụ âm '''

def phan_tich_chuoi(s):
    nguyen_am = "aeiouAEIOU"
    
    chu_in_hoa = sum(c.isupper() for c in s)
    chu_thuong = sum(c.islower() for c in s)
    chu_cai = sum(c.isalpha() for c in s)
    khoang_trang = sum(c.isspace() for c in s)
    ky_tu_dac_biet = sum(not c.isalnum() and not c.isspace() for c in s)

    so_nguyen_am = sum(c in nguyen_am for c in s)
    so_phu_am = sum(c.isalpha() and c not in nguyen_am for c in s)

    print("Số chữ IN HOA:", chu_in_hoa)
    print("Số chữ thường:", chu_thuong)
    print("Số chữ cái:", chu_cai)
    print("Số ký tự đặc biệt:", ky_tu_dac_biet)
    print("Số khoảng trắng:", khoang_trang)
    print("Số nguyên âm:", so_nguyen_am)
    print("Số phụ âm:", so_phu_am)



