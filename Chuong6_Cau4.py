'''Câu 4: Xác định kết quả khi thực thi list 
Yêu cầu: 
Cho list 
lst = [3, 0, 1, 5, 2] 
x = 2 
Hãy cho biết kết quả: 
(a) lst[0]? 
(b) lst[3]? 
(c) lst[x]? 
(d) lst[-x]? 
(e) lst[x + 1]? 
(f) lst[x] + 1? 
(g) lst[lst[x]]? 
(h) lst[lst[lst[x]]]? '''
lst = [3, 0, 1, 5, 2]
x = 2       
a = lst[0]          
b = lst[3]         
c = lst[x]        
d = lst[-x]         
e = lst[x + 1]      
f = lst[x] + 1      
g = lst[lst[x]]     
h = lst[lst[lst[x]]] 
print("a =", a)
print("b =", b)
print("c =", c)
print("d =", d)
print("e =", e)
print("f =", f)
print("g =", g)
print("h =", h)
# Kết quả khi thực thi:
# a = 3
# b = 5
# c = 1
# d = 5
# e = 5
# f = 2
# g = 0
# h = 3





