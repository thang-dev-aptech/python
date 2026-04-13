# biến (variable) : dùng để lưu trữ dữ liệu 
# kiểu dữ liệu (data type) : xác định loại dữ liệu mà biến có thể lưu trữ
# kiểu dữ liệu cơ bản: int, float, str, bool
# kiểu dữ liệu phức tạp: list, tuple, set, dict
# ép kiểu (type casting) : chuyển đổi từ kiểu dữ liệu này sang kiểu dữ liệu khác
# Trong python khai báo biến không cần chỉ định kiểu dữ liệu 

x = 10         # int
y = 3.14       # float
name = "Alice" # str
is_student = True # bool

print(x,y,name,is_student)

# kiểm tra dữ liệu kiểu gì dùng hàm type()
print(type(x))          # <class 'int'>
print(type(y))          # <class 'float'>
print(type(name))       # <class 'str'>
print(type(is_student)) # <class 'bool'>

# chuyển đổi kiểu dữ liệu
a = 5          # int
print(str(a))      # '5' (str)
print(float(a))    # 5.0 (float)

# kiểu nonetype
b = None
print(b)
print(type(b))  # <class 'NoneType'>

# input ()
name = input("Enter your name: ")
print("Hello", name)
