''' Cau9: '''
import math

n = int(input("Nhap n: "))

s = 0
for i in range(n):
    s = math.sqrt(2 + s)

print("S(n) =", s)
