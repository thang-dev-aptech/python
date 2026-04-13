"""
KIẾN THỨC VỀ MATH VÀ DATETIME TRONG PYTHON
------------------------------------------

1. Module `math`:
   - Cung cấp các hàm toán học nâng cao.
   - Các hằng số: pi, e.
   - Các hàm: sqrt, pow, ceil, floor, factorial, ...

2. Module `datetime`:
   - Làm việc với ngày tháng và thời gian.
   - Các class chính: date, time, datetime, timedelta.
   - Định dạng ngày tháng: strftime (date -> string), strptime (string -> date).
"""

import math
import datetime

print("--- 1. Module Math (Toán học) ---")

# Hằng số
print(f"PI: {math.pi}")
print(f"E: {math.e}")

# Các hàm cơ bản
x = 16
print(f"Căn bậc 2 của {x}: {math.sqrt(x)}")  # 4.0

y = 2.3
print(f"Làm tròn lên (ceil) của {y}: {math.ceil(y)}")   # 3
print(f"Làm tròn xuống (floor) của {y}: {math.floor(y)}") # 2

# Lũy thừa
print(f"2 mũ 3 (pow): {math.pow(2, 3)}") # 8.0 (trả về float)

# Giai thừa (Factorial)
n = 5
print(f"Giai thừa của {n} ({n}!): {math.factorial(n)}") # 120

# Trị tuyệt đối (Lưu ý: Python có hàm abs() build-in, math.fabs() trả về float)
print(f"Trị tuyệt đối của -10 (build-in abs): {abs(-10)}")
print(f"Trị tuyệt đối của -10 (math.fabs): {math.fabs(-10)}")


print("\n--- 2. Module Datetime (Ngày giờ) ---")

# Lấy thời gian hiện tại
now = datetime.datetime.now()
print(f"Thời gian hiện tại: {now}")
print(f"Năm: {now.year}, Tháng: {now.month}, Ngày: {now.day}")
print(f"Giờ: {now.hour}, Phút: {now.minute}, Giây: {now.second}")

# Tạo một ngày cụ thể
my_birthday = datetime.datetime(2000, 1, 15)  # Năm, Tháng, Ngày
print(f"Sinh nhật (cố định): {my_birthday}")

# Định dạng ngày tháng (Format date) -> String
# %Y: Năm (4 số), %m: Tháng, %d: Ngày, %H: Giờ (24h), %M: Phút, %S: Giây
formatted_date = now.strftime("%d/%m/%Y %H:%M:%S")
print(f"Định dạng kiểu VN: {formatted_date}")

# Parse chuỗi thành ngày tháng (String -> Date)
date_str = "15/01/2000"
date_object = datetime.datetime.strptime(date_str, "%d/%m/%Y")
print(f"Chuyển chuỗi '{date_str}' thành object: {date_object}")

# Tính toán thời gian (timedelta)
# Cộng/Trừ thời gian
tomorrow = now + datetime.timedelta(days=1)
print(f"Ngày mai là: {tomorrow}")

one_week_ago = now - datetime.timedelta(weeks=1)
print(f"Một tuần trước là: {one_week_ago}")

# Khoảng cách giữa 2 ngày
diff = now - my_birthday
print(f"Tôi đã sống được: {diff.days} ngày")
