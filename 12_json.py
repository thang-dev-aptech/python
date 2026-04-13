import json

# JSON (JavaScript Object Notation) là một định dạng dữ liệu nhẹ dùng để trao đổi dữ liệu.
# Python cung cấp module `json` tích hợp sẵn để làm việc với dữ liệu JSON.

# --- 1. Chuyển đổi từ Python sang JSON (Serialization) ---
# Hàm `json.dumps()`: chuyển đổi object Python thành chuỗi JSON.

data = {
    "name": "Nguyen Van A",
    "age": 25,
    "city": "Ho Chi Minh",
    "is_student": False,
    "grades": [8.5, 9.0, 7.5],
    "address": {
        "street": "Nguyen Hue",
        "district": 1
    },
    "none_value": None
}

# Chuyển đổi sang chuỗi JSON
# Lưu ý: Kết quả là một chuỗi (str)
json_string = json.dumps(data)
print("1. JSON String:", json_string)

# Định dạng đẹp (Pretty Print) với indent
# ensure_ascii=False để hiển thị tiếng Việt đúng, không bị mã hóa thành unicode escape
json_string_pretty = json.dumps(data, indent=4, ensure_ascii=False)
print("\n2. JSON String (Pretty):")
print(json_string_pretty)

# Sắp xếp các khóa (sort_keys)
json_string_sorted = json.dumps(data, indent=4, sort_keys=True)
print("\n3. JSON String (Sorted Keys):")
print(json_string_sorted)

# --- 2. Chuyển đổi từ JSON sang Python (Deserialization) ---
# Hàm `json.loads()`: chuyển đổi chuỗi JSON thành object Python (thường là dict hoặc list).

json_input = '{"name": "Tran Van B", "age": 30, "skills": ["Python", "Django"]}'
python_obj = json.loads(json_input)

print("\n4. Python Object from JSON string:", python_obj)
print("   Kiểu dữ liệu:", type(python_obj))
print("   Truy cập dữ liệu:", python_obj["name"], "-", python_obj["skills"][0])

# --- 3. Làm việc với file JSON ---

# Ghi dữ liệu vào file JSON: `json.dump()` (không có chữ 's' ở cuối)
file_path = "data.json"
try:
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print(f"\n5. Đã ghi dữ liệu vào file '{file_path}'")
except Exception as e:
    print(f"Lỗi khi ghi file: {e}")

# Đọc dữ liệu từ file JSON: `json.load()` (không có chữ 's' ở cuối)
try:
    with open(file_path, "r", encoding="utf-8") as f:
        loaded_data = json.load(f)
    print("\n6. Đã đọc dữ liệu từ file:")
    print(loaded_data)
except FileNotFoundError:
    print(f"File '{file_path}' không tồn tại.")
except json.JSONDecodeError:
    print("Lỗi định dạng JSON trong file.")

# --- Bảng tương đương kiểu dữ liệu ---
# Python           JSON
# dict             object
# list, tuple      array
# str              string
# int, float       number (int, real)
# True             true
# False            false
# None             null
