# ============================================================
# PYTHON CHEATSHEET - PHẦN 7: MODULES & PACKAGES
# ============================================================

# --- 1. Import module chuẩn ---
import math
print("Căn bậc 2 của 16:", math.sqrt(16))
print("Số pi:", math.pi)

# --- 2. Import một phần của module ---
from math import sqrt, pow
print("sqrt(25):", sqrt(25))
print("pow(2,3):", pow(2,3))

# --- 3. Đặt alias (tên ngắn gọn) ---
import math as m
print("cos(0):", m.cos(0))

# --- 4. Import tất cả (không khuyến khích) ---
# from math import *   # dễ gây xung đột tên

# --- 5. Một số module built-in khác ---
import random
print("Ngẫu nhiên từ 1-100:", random.randint(1, 100))

import datetime
today = datetime.date.today()
print("Hôm nay là:", today)

import sys
print("Version Python:", sys.version)

# --- 6. Tạo module riêng ---
# Giả sử bạn tạo file mymodule.py cùng thư mục với file này:
# Nội dung file mymodule.py:
#   def say_hello(name):
#       print(f"Hello, {name}!")
#
# Sau đó có thể import như sau:

# import mymodule
# mymodule.say_hello("Python")

# --- 7. Package ---
# Package là thư mục chứa nhiều module + file __init__.py
# Ví dụ cấu trúc:
#   mypackage/
#       __init__.py
#       module1.py
#       module2.py
#
# Khi đó có thể import:
#   from mypackage import module1
#   from mypackage.module2 import func_x

