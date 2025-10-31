'''Câu 6: Nhập một số n có tối đa 2 chữ số. Hãy cho biết cách đọc ra dạng chữ.  
(vd: n=35 => Ba mươi lăm, n=5 => năm). '''
n = int(input("Nhập số (0 - 99): "))

if n < 0 or n > 99:
    print("Ngoài phạm vi")
else:
    chuc = n // 10
    dv = n % 10

    if n < 10:  # Một chữ số
        if n == 0: print("Không")
        elif n == 1: print("Một")
        elif n == 2: print("Hai")
        elif n == 3: print("Ba")
        elif n == 4: print("Bốn")
        elif n == 5: print("Năm")
        elif n == 6: print("Sáu")
        elif n == 7: print("Bảy")
        elif n == 8: print("Tám")
        elif n == 9: print("Chín")

    elif n < 20:  # Từ 10 đến 19
        if n == 10: print("Mười")
        elif n == 15: print("Mười lăm")
        else:
            print("Mười", end=" ")
            if dv == 1: print("một")
            elif dv == 4: print("bốn")
            elif dv == 5: print("lăm")
            else:
                print(["","một","hai","ba","bốn","năm","sáu","bảy","tám","chín"][dv])

    else:  # Từ 20 đến 99
        if chuc == 2: print("Hai mươi", end=" ")
        elif chuc == 3: print("Ba mươi", end=" ")
        elif chuc == 4: print("Bốn mươi", end=" ")
        elif chuc == 5: print("Năm mươi", end=" ")
        elif chuc == 6: print("Sáu mươi", end=" ")
        elif chuc == 7: print("Bảy mươi", end=" ")
        elif chuc == 8: print("Tám mươi", end=" ")
        elif chuc == 9: print("Chín mươi", end=" ")

        if dv == 0: print("")
        elif dv == 1: print("mốt")
        elif dv == 4: print("bốn")
        elif dv == 5: print("lăm")
        else:
            print(["","một","hai","ba","bốn","năm","sáu","bảy","tám","chín"][dv])

