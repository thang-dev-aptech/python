# Collections (danh sách)
# Bao gồm : list, tuple, set, dictionary 

# --- 1. List ---

fruits = ["apple", "banana", "cherry"]
print(fruits)

# Truy cập phần tử
print(fruits[0])    # apple
print(fruits[-1])   # cherry (phần tử cuối)

# Cắt list
print(fruits[0:2])  # ['apple', 'banana']

# Thêm phần tử
fruits.append("mango")    # thêm cuối
fruits.insert(1, "orange") # thêm tại vị trí
print(fruits)

# Xóa phần tử
fruits.remove("banana")   # xóa theo giá trị
print(fruits)
fruits.pop()              # xóa phần tử cuối
print(fruits)
del fruits[0]             # xóa phần tử theo index
print(fruits)

# Duyệt list
for f in fruits:
    print("Fruit:", f)

# List comprehension (cách viết ngắn gọn)
squares = [x**2 for x in range(5)]
print("Squares:", squares)


# --- 2. Tuple (bất biến - immutable) ---

numbers = (1, 2, 3, 4)
print(numbers[0])
print(numbers[-1])

# Tuple không thể thay đổi
# numbers[0] = 10  # lỗi

# Tuple unpacking
a, b, c, d = numbers
print(a, b, c, d)


# --- 3. Set (tập hợp - không trùng lặp, không có thứ tự) ---
myset = {1,3,3,2,2,4}
print(myset) 

# Thêm / xóa phần tử
myset.add(4)
print(myset)
myset.remove(2)
print(myset)

# Toán tập hợp
A = {1, 2, 3}
B = {3, 4, 5}
print("Hợp:", A | B)       # {1,2,3,4,5}
print("Giao:", A & B)      # {3}
print("Hiệu:", A - B)      # {1,2}
print("Đối xứng:", A ^ B)  # {1,2,4,5}


# --- 4. Dictionary (từ điển - key:value) ---

person = {
    "name": "Alice",
    "age": 25,
    "job": "Developer"
}
print(person)

# Truy cập value
print(person["name"])
print(person.get("age"))

# Thêm / sửa key
person["city"] = "Hanoi"
person["age"] = 26
print(person)

# Xóa key
del person["job"]
print(person)

# Duyệt dictionary
for k, v in person.items():
    print(k, ":", v)

# Dictionary comprehension
squares_dict = {x: x**2 for x in range(5)}
print("Squares dict:", squares_dict)



