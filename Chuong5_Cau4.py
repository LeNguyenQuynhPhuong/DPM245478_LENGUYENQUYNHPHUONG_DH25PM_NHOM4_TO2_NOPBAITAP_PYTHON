'''Câu 4: Các hàm quan trọng trong xử lý chuỗi của Python
Trang 47/84
Yêu cầu:
Trình bày một số hàm quan trọng trong xử lý Chuỗi của Python'''
# Một số hàm quan trọng trong xử lý chuỗi của Python
# 1. len(): Trả về độ dài của chuỗi
s = "Hello, World!"
print(len(s))  # Output: 13
# 2. str(): Chuyển đổi giá trị thành chuỗi
num = 123
print(str(num))  # Output: '123'
# 3. lower(): Chuyển đổi chuỗi thành chữ thường
print(s.lower())  # Output: 'hello, world!'
# 4. upper(): Chuyển đổi chuỗi thành chữ hoa
print(s.upper())  # Output: 'HELLO, WORLD!'
# 5. strip(): Loại bỏ khoảng trắng ở đầu và cuối chuỗi
s_with_spaces = "   Hello, World!   "
print(s_with_spaces.strip())  # Output: 'Hello, World!'
# 6. replace(): Thay thế một phần của chuỗi bằng một chuỗi khác
print(s.replace("World", "Python"))  # Output: 'Hello, Python!'
# 7. split(): Chia chuỗi thành một danh sách con dựa trên một ký tự phân tách
print(s.split(", "))  # Output: ['Hello', 'World!']
# 8. join(): Nối các phần tử trong một danh sách thành một chuỗi, sử dụng chuỗi hiện tại làm ký tự phân tách
words = ['Hello', 'World!']
print(" ".join(words))  # Output: 'Hello World!'
# 9. find(): Tìm vị trí xuất hiện đầu tiên của một chuỗi con trong chuỗi
print(s.find("World"))  # Output: 7
# 10. isdigit(): Kiểm tra xem tất cả các ký tự trong chuỗi
print("12345".isdigit())  # Output: True
# có phải là chữ số hay không
print("Hello".isdigit())  # Output: False

