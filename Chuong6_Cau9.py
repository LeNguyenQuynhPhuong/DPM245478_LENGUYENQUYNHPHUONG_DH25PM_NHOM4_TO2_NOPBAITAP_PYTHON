'''Câu 9: Xử lý mảng 
Yêu cầu: 
Viết chương trình nhập vào một mảng số tự nhiên. Hãy xuất ra màn hình:  - Dòng 1 : gồm các số lẻ, tổng cộng có bao nhiêu số lẻ.  - Dòng 2 : gồm các số chẵn, tổng cộng có bao nhiêu số chẵn.  - Dòng 3 : gồm các số nguyên tố.  - Dòng 4 : gồm các số không phải là số nguyên tố.  
M[] ={3,6,7,8,11,17,2,90,2,5,4,5,8} 
➔ 3, 7, 11,17, 5(2) ➔6 số lẻ'''
M = [3, 6, 7, 8, 11, 17, 2, 90, 2, 5, 4, 5, 8]
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
odd_numbers = []
even_numbers = []
prime_numbers = []
non_prime_numbers = []
for num in M:
    if num % 2 != 0:
        odd_numbers.append(num)
    else:
        even_numbers.append(num)
    if is_prime(num):
        prime_numbers.append(num)
    else:
        non_prime_numbers.append(num)
print("Dòng 1: Số lẻ:", odd_numbers, "Tổng số lẻ:", len(odd_numbers))
print("Dòng 2: Số chẵn:", even_numbers, "Tổng số chẵn:", len(even_numbers))
print("Dòng 3: Số nguyên tố:", prime_numbers)
print("Dòng 4: Số không phải là số nguyên tố:", non_prime_numbers)
