'''Câu 6: Nhập vào 1 list có N số ngẫu nhiên KHÔNG TRÙNG NHAU'''
from random import randrange
def TaoList(N):
    lst = []
    while len(lst) < N:
        num = randrange(1, N*10)
        if num not in lst:
            lst.append(num)
    return lst
N = int(input("Nhập số phần tử N của list: "))
result_list = TaoList(N)
print("List ngẫu nhiên không trùng nhau:", result_list)
