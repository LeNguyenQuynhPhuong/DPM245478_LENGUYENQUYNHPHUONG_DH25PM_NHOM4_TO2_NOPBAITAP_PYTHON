'''Câu 18: Vẽ các hình dưới đây '''
# hinh vuong rong
for i in range(5):
    for j in range(5):
        if i == 0 or i == 4 or j == 0 or j == 4:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
    # hinh tam giac phai
n = 4
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)

#hinh tam giac trai
n = 4
for i in range(1, n + 1):
    print("*" * i)

