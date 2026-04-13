# ============================================================
# PYTHON CHEATSHEET - PHẦN 18: COMPREHENSIONS & NGỮ PHÁP NGẮN GỌN
# ============================================================

# Giới thiệu:
# List Comprehension là cách viết code ngắn gọn, "Pythonic" để tạo list mới từ list cũ.
# Giúp code dễ đọc hơn (nếu không lạm dụng) và thường chạy nhanh hơn vòng for thông thường.

# ============================================================
# 1. LIST COMPREHENSION
# ============================================================
print("--- 1. List Comprehension ---")

numbers = [1, 2, 3, 4, 5]

# Cách truyền thống (dùng vòng lặp for)
squares_v1 = []
for n in numbers:
    squares_v1.append(n * n)

# Cách dùng List Comprehension
# Cú pháp: [expression for item in iterable]
squares_v2 = [n * n for n in numbers]

print(f"Gốc: {numbers}")
print(f"Bình phương (v1): {squares_v1}")
print(f"Bình phương (v2): {squares_v2}")

# Có thêm điều kiện (if)
# Cú pháp: [expression for item in iterable if condition]
# Lấy số chẵn và nhân đôi
even_doubles = [n * 2 for n in numbers if n % 2 == 0]
print(f"Số chẵn nhân đôi: {even_doubles}")

# Có cả if và else (Ternary Operator trong Comprehension)
# Cú pháp: [val_true if cond else val_false for item in iterable]
# Nếu chẵn thì giữ nguyên, lẻ thì thay bằng số 0
parity_check = [n if n % 2 == 0 else 0 for n in numbers]
print(f"Giữ chẵn, lẻ thành 0: {parity_check}")

# ============================================================
# 2. DICTIONARY & SET COMPREHENSION
# ============================================================
print("\n--- 2. Dict & Set Comprehension ---")

names = ["Alice", "Bob", "Charlie"]

# Dict Comprehension
# Tạo dict với key là tên, value là độ dài tên
name_lengths = {name: len(name) for name in names}
print(f"Độ dài tên (Dict): {name_lengths}")

# Set Comprehension (tạo set, tự động loại bỏ trùng lặp)
nums = [1, 2, 2, 3, 4, 4, 5]
unique_squares = {n * n for n in nums}
print(f"Set bình phương (duy nhất): {unique_squares}")

# ============================================================
# 3. ENUMERATE (DUYỆT KÈM CHỈ SỐ)
# ============================================================
print("\n--- 3. Enumerate ---")

fruits = ["Tao", "Chuoi", "Cam"]

# Thay vì dùng: for i in range(len(fruits)): ...
for index, value in enumerate(fruits, start=1):
    print(f"STT {index}: {value}")

# ============================================================
# 4. ZIP (GỘP NHIỀU LIST)
# ============================================================
print("\n--- 4. Zip ---")

students = ["An", "Binh", "Chi"]
scores = [8.5, 9.0, 7.5]

# Ghép 2 list lại thành từng cặp
zipped = zip(students, scores)
print(f"Zipped object: {zipped}") 
# Lưu ý: zip trả về iterator, muốn xem phải ép kiểu sang list hoặc duyệt qua
print(f"List zipped: {list(zip(students, scores))}")

# Duyệt song song 2 list
for name, score in zip(students, scores):
    print(f"{name} đạt điểm: {score}")

# ============================================================
# 5. TOÁN TỬ 3 NGÔI (TERNARY OPERATOR)
# ============================================================
print("\n--- 5. Ternary Operator ---")

age = 18
# Cú pháp: value_if_true if condition else value_if_false
status = "Đủ tuổi" if age >= 18 else "Chưa đủ tuổi"
print(f"Tuổi {age}: {status}")

# ============================================================
# 6. UNPACKING (GIẢI NÉN BIẾN)
# ============================================================
print("\n--- 6. Unpacking ---")

# Unacking Tuple/List
coords = (10, 20)
x, y = coords
print(f"x={x}, y={y}")

# Dùng dấu * để lấy phần còn lại
first, *middle, last = [1, 2, 3, 4, 5, 6]
print(f"First: {first}")
print(f"Middle: {middle}")
print(f"Last: {last}")

# Gộp dict (Python 3.9+)
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged = dict1 | dict2  # dict2 sẽ ghi đè dict1 nếu trùng key
print(f"Merged Digt (|): {merged}")
