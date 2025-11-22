'''Câu 6: Trích lọc số âm trong chuỗi
Yêu cầu:
Viết một hàm đặt tên là NegativeNumberInStrings(str). Hàm này có đối số truyền vào
là một chuỗi bất kỳ, Hãy viết lệnh để xuất ra các số nguyên âm trong chuỗi.
Ví dụ: Nếu nhập vào chuỗi “abc-5xyz-12k9l--p” thì hàm phải xuất ra được 2 số nguyên
âm đó là -5 và -12 '''
import re

def NegativeNumberInStrings(chuoi):
    ket_qua = re.findall(r"-\d+", chuoi)
    return [int(x) for x in ket_qua]


# Ví dụ 
chuoi_vi_du = "abc-5xyz-12k91-p"
print(NegativeNumberInStrings(chuoi_vi_du))
