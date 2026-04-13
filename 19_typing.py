# ============================================================
# PYTHON CHEATSHEET - PHẦN 19: TYPE HINTS (GỢI Ý KIỂU DỮ LIỆU)
# ============================================================

# Giới thiệu:
# Python là ngôn ngữ "Dynamic Typing" (kiểu động), không bắt buộc khai báo kiểu.
# Tuy nhiên, từ Python 3.5+, ta có thể thêm "Type Hints" để code rõ ràng hơn,
# giúp IDE gợi ý code tốt hơn và phát hiện lỗi sớm.

from typing import List, Dict, Set, Tuple, Optional, Union, Any

# ============================================================
# 1. CÚ PHÁP CƠ BẢN
# ============================================================
print("--- 1. Basic Type Hints ---")

# Biến (Variable)
age: int = 25
name: str = "Nguyen Van A"
height: float = 1.75
is_student: bool = True

print(f"{name} ({age} tuổi) - Student: {is_student}")

# Hàm (Function)
# Cú pháp: def func(arg: type) -> return_type:
def add(a: int, b: int) -> int:
    return a + b

print(f"Tổng: {add(10, 20)}")
# Lưu ý: Python KHÔNG QUĂNG LỖI nếu bạn truyền sai kiểu lúc chạy (Runtime).
# Type Hint chỉ có tác dụng documentation và check tĩnh (như mypy, Pylance).
# print(add("10", "20")) # Vẫn chạy ra "1020" dù sai logic gợi ý.


# ============================================================
# 2. KIỂU DỮ LIỆU CẤU TRÚC (LIST, DICT, TUPLE)
# ============================================================
print("\n--- 2. List, Dict, Tuple ---")

# List chứa toàn số nguyên
# (Từ Python 3.9+ có thể dùng list[int] thay vì List[int])
scores: List[int] = [10, 8, 9]

# Dict với key là string, value là float
prices: Dict[str, float] = {
    "apple": 1.5,
    "banana": 0.8
}

# Tuple cố định số lượng phần tử và kiểu
coordinate: Tuple[int, int] = (10, 20)
user_info: Tuple[str, int, bool] = ("Alice", 25, True)

print(f"Scores: {scores}")


# ============================================================
# 3. TYPE NÂNG CAO (OPTIONAL, UNION, ANY)
# ============================================================
print("\n--- 3. Advanced Types ---")

# 3.1. Union: Chấp nhận nhiều kiểu dữ liệu
# Ví dụ: ID có thể là số hoặc chuỗi
def process_id(user_id: Union[int, str]) -> None:
    print(f"Processing ID: {user_id}")

process_id(101)
process_id("USER_101")
# (Python 3.10+ có thể viết: int | str)

# 3.2. Optional: Có thể là kiểu dữ liệu đó HOẶC None
def find_user(name: str) -> Optional[str]:
    db = {"Alice": "Alice in Wonderland", "Bob": "Bob the Builder"}
    return db.get(name) # Trả về str nếu có, None nếu không

res1 = find_user("Alice")
res2 = find_user("Charlie")
print(f"Found: {res1}")
print(f"Found: {res2}") # None

# 3.3. Any: Chấp nhận MỌI kiểu (dùng khi không xác định được)
# Hạn chế dùng vì nó làm mất tác dụng của Type Hint
def print_anything(data: Any):
    print(f"Data: {data}")


# ============================================================
# 4. CLASS TYPE (KIỂU ĐỐI TƯỢNG)
# ============================================================
print("\n--- 4. Class Type Hint ---")

class Student:
    def __init__(self, name: str):
        self.name = name

def register_student(s: Student) -> None:
    print(f"Đăng ký cho học viên: {s.name}")

st = Student("Nam")
register_student(st)


# ============================================================
# 5. ALIAS (ĐỊNH NGHĨA APP KIỂU RIÊNG)
# ============================================================
print("\n--- 5. Type Alias ---")

# Định nghĩa một cấu trúc phức tạp thành tên ngắn gọn
Vector = List[float]
UserDict = Dict[str, Union[str, int]]

def move(v: Vector):
    print(f"Moving vector: {v}")

vec: Vector = [1.0, 2.5, 3.1]
move(vec)
