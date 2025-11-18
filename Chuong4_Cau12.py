'''Câu 12: Hàm oscillate 
Yêu cầu: 
Cho mã lệnh: 
Hãy viết hàm oscillate để khi chạy phần mềm, nó ra kết quả: -3   3   -2   
2   -1   
1   0   0   1   -1   2   -2   3   -3   4   -4'''
def oscillate(a, b):
   
    for i in range(a, abs(a) + 1):
        yield i
    
   
    for i in range(abs(a), a - 1, -1):
        yield i
     
    for i in range(a, b + 1):
        yield i
for n in oscillate(-3, 5):
    print(n, end=' ')
print()
