'''Câu 10: Vẽ hình dùng Sleep 
Yêu cầu: 
Vẽ 4 hình dưới đây, dùng sleep để xuất hiện từng hình sau 5 giây'''
import time
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def hinh1():
    print("        *        ")
    print("      *   *      ")
    print("    *       *    ")
    print("  *           *  ")
    print("* * * * * * * * *")

def hinh2():
    print("* * * * * * * * *")
    print("  *           *  ")
    print("    *       *    ")
    print("      *   *      ")
    print("        *        ")

def hinh3():
    print("    *       *    ")
    print("    *       *    ")
    print("*****************")
    print("    *       *    ")
    print("    *       *    ")

def hinh4():
    print(" *   *   *   *   *")
    print("   *   *   *   *  ")
    print(" *   *   *   *   *")
    print("   *   *   *   *  ")
    print(" *   *   *   *   *")

clear()
hinh1()
time.sleep(5)

clear()
hinh2()
time.sleep(5)

clear()
hinh3()
time.sleep(5)

clear()
hinh4()
time.sleep(5)
