# toán tử (operator)

# --- 1. Toán tử số học (Arithmetic Operators) ---
a, b = 10, 3

print("a + b =", a + b)   # cộng
print("a - b =", a - b)   # trừ
print("a * b =", a * b)   # nhân
print("a / b =", a / b)   # chia (luôn ra float)
print("a // b =", a // b) # chia lấy nguyên
print("a % b =", a % b)   # chia lấy dư
print("a ** b =", a ** b) # lũy thừa (a mũ b)

# --- 2. Toán tử so sánh (Comparison Operators) ---
# Kết quả trả về True hoặc False
print("a == b ?", a == b) # bằng
print("a != b ?", a != b) # khác
print("a > b ?", a > b)   # lớn hơn
print("a < b ?", a < b)   # nhỏ hơn
print("a >= b ?", a >= b) # lớn hơn hoặc bằng
print("a <= b ?", a <= b) # nhỏ hơn hoặc bằng

# --- 3. Toán tử logic (Logical Operators) ---
x, y = True, False
print("x and y =", x and y) # cả 2 True thì mới True
print("x or y =", x or y)   # 1 trong 2 True thì True
print("not x =", not x)     # đảo ngược giá trị

# --- 4. Toán tử gán (Assignment Operators) ---
c = 5
c += 2   # tương đương c = c + 2
print("c =", c)
c *= 3   # c = c * 3
print("c =", c)

# --- 5. Toán tử thành viên (Membership Operators) ---
fruits = ["apple", "banana", "mango"]
print("'apple' in fruits ?", "apple" in fruits)      # True
print("'orange' not in fruits ?", "orange" not in fruits)  # True

# --- 6. Toán tử định danh (Identity Operators) ---
# Kiểm tra 2 biến có cùng trỏ đến 1 object trong bộ nhớ hay không
m = [1, 2, 3]
n = m          # cùng tham chiếu
k = [1, 2, 3]  # khác tham chiếu

print("m is n ?", m is n)       # True (cùng object)
print("m is k ?", m is k)       # False (khác object)
print("m == k ?", m == k)       # True (giá trị giống nhau)