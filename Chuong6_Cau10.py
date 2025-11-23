'''Câu 10: Xử lý Ma Trận 
Yêu cầu: 
Nhập 2 matrix A, B. 
Cộng 2 matrix 
Viết hàm tính matrix hoán vị➔áp dụng để tìm cho A, B '''
def NhapMaTran(rows, cols, name):
    print(f"Nhập ma trận {name} ({rows}x{cols}):")
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            value = float(input(f"Nhập phần tử [{i+1}][{j+1}]: "))
            row.append(value)
        matrix.append(row)
    return matrix
def CongMaTran(A, B):
    rows = len(A)
    cols = len(A[0])
    C = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(A[i][j] + B[i][j])
        C.append(row)
    return C
def HoanViMaTran(M):
    rows = len(M)
    cols = len(M[0])
    HT = []
    for j in range(cols):
        row = []
        for i in range(rows):
            row.append(M[i][j])
        HT.append(row)
    return HT
rows = int(input("Nhập số hàng của ma trận: "))
cols = int(input("Nhập số cột của ma trận: "))
A = NhapMaTran(rows, cols, "A")
B = NhapMaTran(rows, cols, "B")
C = CongMaTran(A, B)
print("Ma trận A + B là:")
for row in C:
    print(row)
HT_A = HoanViMaTran(A)
HT_B = HoanViMaTran(B)
print("Ma trận hoán vị của A là:")
for row in HT_A:
    print(row)
print("Ma trận hoán vị của B là:")
for row in HT_B:
    print(row)
    