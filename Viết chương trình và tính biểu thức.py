# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 15:35:29 2024

@author: Nguyễn Xuân Hoan - 23694771
"""

import math
a = float(input("Nhập giá trị a: "))
b = float(input("Nhập giá trị b: "))
A = (math.sqrt(a) - math.sqrt(b) / math.sqrt(math.sqrt(a)) - math.sqrt(math.sqrt(b))) - (math.sqrt(a) + math.sqrt(math.sqrt(a*b)) / math.sqrt(math.sqrt(a)) + math.sqrt(math.sqrt(b)) )
print("Kết quả: ", A)




