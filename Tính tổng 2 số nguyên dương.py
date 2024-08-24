# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 14:07:16 2024

@author: Nguyễn Xuân Hoan - 23694771
"""

N = float(input("Nhập giá trị N: "))
a = N//10
b = N%10
if N > 9 and N < 99:
    print("Tổng 2 số là: ", a+b)
else:
    print("Số của bạn nhập không hợp lệ")
    
        


