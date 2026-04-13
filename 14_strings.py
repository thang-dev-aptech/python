# ============================================================
# PYTHON CHEATSHEET - PHẦN 3: CHUỖI (STRINGS)
# ============================================================

# --- 1. Khai báo chuỗi ---
s1 = "Hello"
s2 = 'World'
s3 = """Chuỗi nhiều dòng
có thể viết thoải mái
không cần \n"""
print(s1)
print(s2)
print(s3)

# --- 2. Nối chuỗi ---
name = "Python"
msg = "Hello " + name
print(msg)

# --- 3. Độ dài chuỗi ---
print("Độ dài của msg:", len(msg))

# --- 4. Truy cập ký tự ---
word = "Python"
print(word[0])   # ký tự đầu tiên
print(word[-1])  # ký tự cuối cùng
print(word[0:3]) # cắt chuỗi từ 0 đến 2 -> "Pyt"
print(word[:4])  # từ đầu đến index 3 -> "Pyth"
print(word[2:])  # từ index 2 đến hết -> "thon"

# --- 5. Duyệt chuỗi ---
for ch in word:
    print(ch)

# --- 6. Một số method hữu ích ---
text = "  hello world  "
print(text.upper())      # HELLO WORLD
print(text.lower())      # hello world
print(text.title())      # Hello World
print(text.strip())      # xóa khoảng trắng đầu + cuối
print(text.replace("world", "Python"))  # thay thế
print("world" in text)   # kiểm tra có "world" không
print("Python" not in text)

# --- 7. Tách và ghép chuỗi ---
data = "apple,banana,cherry"
fruits = data.split(",")   # tách thành list
print(fruits)

joined = "-".join(fruits)  # ghép list thành chuỗi
print(joined)

# --- 8. Chuỗi format ---
name = "Alice"
age = 25

# Cách 1: f-string (Python 3.6+)
print(f"My name is {name}, I am {age} years old.")

# Cách 2: format()
print("My name is {}, I am {} years old.".format(name, age))
print("My name is {n}, I am {a}".format(n=name, a=age))

# --- 9. Escape characters ---
quote = "He said: \"Python is fun!\""
path = "C:\\Users\\Admin"
print(quote)
print(path)

# --- 10. Kiểm tra nội dung chuỗi ---
s = "Python123"
print(s.isalpha())   # False (có cả chữ + số)
print("Python".isalpha())  # True (chỉ chữ)
print(s.isdigit())   # False
print("123".isdigit())  # True
print(s.isalnum())   # True (chữ + số)
print("   ".isspace())   # True (toàn khoảng trắng)

# --- 11. Đảo chuỗi nhanh ---
rev = word[::-1]
print("Chuỗi gốc:", word)
print("Chuỗi đảo:", rev)

