''' 
Câu 8: Viết chương trình nhập vào một dãy n số thực M[0], M[1],..., M[n-1], sắp xếp 
dãy số theo thứ tự giảm dần. Xuất ra dãy số sau khi sắp xếp.'''
def NhapDaySo(n):
    day_so = []
    for i in range(n):
        num = float(input(f"Nhập số thực thứ {i + 1}: "))
        day_so.append(num)
    return day_so
def SapXepGiamDan(day_so):
    n = len(day_so)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if day_so[i] < day_so[j]:
                day_so[i], day_so[j] = day_so[j], day_so[i]
    return day_so
n = int(input("Nhập số lượng phần tử trong dãy số: "))
day_so = NhapDaySo(n)
day_so_sap_xep = SapXepGiamDan(day_so)
print("Dãy số sau khi sắp xếp theo thứ tự giảm dần là:", day_so_sap_xep)
5