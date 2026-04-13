# PYTHON BASE KNOWLEDGE MAP

Mục tiêu của file này là tóm tắt **toàn bộ kiến thức đã học trong folder Python** theo từng file, để:
- ôn nhanh trước khi làm bài tập
- nhìn lại bức tranh tổng quát
- dễ up lên Git để sang máy khác vẫn xem được

---

# Tổng quan cả bộ

Bộ tài liệu hiện tại đi theo 3 lớp:

1. **Core syntax** (`1 -> 9`)
   - học cú pháp nền tảng của Python
   - cách Python xử lý dữ liệu
   - function, loop, collections, iterator

2. **Làm việc thực tế với dữ liệu và môi trường** (`10 -> 17`)
   - module/package
   - datetime, json, regex
   - file I/O
   - exceptions
   - pip / virtualenv

3. **Viết Python gọn và rõ hơn** (`18 -> 19`)
   - comprehension
   - enumerate / zip / unpacking
   - type hints

---

# FILE-BY-FILE SUMMARY

## 1. `1_bien_kieu_du_lieu.py`
### Nội dung
- Biến trong Python
- Kiểu dữ liệu cơ bản: `int`, `float`, `str`, `bool`
- Ép kiểu: `str()`, `float()`, ...
- `None`
- `type()`
- `input()`

### Cần nhớ
- Python là ngôn ngữ **dynamic typing**
- `input()` luôn trả về `str`
- `None` là giá trị “không có gì”, không giống `0` hay `""`

### Mức độ quan trọng
**Rất quan trọng** — đây là nền móng

---

## 2. `2_toan_tu.py`
### Nội dung
- Toán tử số học: `+ - * / // % **`
- Toán tử so sánh: `== != > < >= <=`
- Toán tử logic: `and`, `or`, `not`
- Toán tử gán
- Membership: `in`, `not in`
- Identity: `is`, `is not`

### Cần nhớ
- `==` so sánh giá trị
- `is` so sánh object
- `%` là chia lấy dư
- `//` là chia lấy phần nguyên

### Mức độ quan trọng
**Rất quan trọng**

---

## 3. `3_collections.py`
### Nội dung
- `list`
- `tuple`
- `set`
- `dict`
- thêm, sửa, xóa, duyệt dữ liệu
- comprehension cơ bản

### Cần nhớ
- `list`: có thứ tự, sửa được
- `tuple`: có thứ tự, không sửa được
- `set`: không trùng lặp
- `dict`: key-value

### Mức độ quan trọng
**Cực kỳ quan trọng**

---

## 4. `4_cau_dieu_kien.py`
### Nội dung
- `if / elif / else`
- toán tử 3 ngôi
- `match / case`

### Cần nhớ
- `if/elif/else` là flow điều kiện cơ bản
- ternary chỉ nên dùng cho logic ngắn
- `match/case` giống `switch-case`

### Mức độ quan trọng
**Rất quan trọng**

---

## 5. `5_vong_lap.py`
### Nội dung
- `while`
- `for`
- `break`
- `continue`
- `for...else`
- nested loop

### Cần nhớ
- `for` dùng để duyệt iterable
- `while` dùng khi chưa biết trước số lần lặp
- `break` dừng vòng lặp
- `continue` bỏ qua vòng hiện tại
- `for...else` chạy `else` nếu loop không bị `break`

### Mức độ quan trọng
**Rất quan trọng**

---

## 6. `6_ham.py`
### Nội dung
- định nghĩa hàm bằng `def`
- tham số và giá trị trả về
- tham số mặc định
- `*args`, `**kwargs`
- scope local / global
- decorator
- lambda
- recursion
- generator
- hàm nhận hàm khác làm đối số

### Cần nhớ
- `return` kết thúc hàm và trả kết quả
- ưu tiên viết function rõ ràng, chia nhỏ logic
- `*args` nhận nhiều positional arguments
- `**kwargs` nhận nhiều named arguments
- recursion phải có điểm dừng
- generator dùng `yield`

### Mức độ quan trọng
**Cực kỳ quan trọng**

### Ghi chú
- Decorator nên biết khái niệm trước, chưa cần master ngay ở base

---

## 7. `7_ham_range.py`
### Nội dung
- `range(start, stop, step)`
- dùng `range` trong vòng lặp
- slicing với `range`
- membership trên `range`
- độ dài của `range`

### Cần nhớ
- `stop` không được lấy
- `step` là bước nhảy
- `range` hay đi với `for`

### Mức độ quan trọng
**Quan trọng vừa**

---

## 8. `8_mang.py`
### Nội dung
- các thao tác với list:
  - `len()`
  - `max()`
  - `min()`
  - `sort()`
  - `reverse()`
  - `append()`
  - `remove()`
  - `pop()`
  - `index()`
  - `count()`
  - `copy()`
  - `clear()`
- `del`

### Cần nhớ
- `sort()` sửa trực tiếp list gốc
- `sorted()` trả list mới
- `append()` thêm cuối list
- `pop()` xóa theo index hoặc cuối list
- `remove()` xóa theo giá trị

### Mức độ quan trọng
**Rất quan trọng**

---

## 9. `9_iterator.py`
### Nội dung
- iterable vs iterator
- `iter()`
- `next()`
- `StopIteration`
- custom iterator
- generator
- infinite iterator

### Cần nhớ
- `for` loop hoạt động dựa trên iterator
- iterable là đối tượng lặp được
- iterator là đối tượng trả ra từng phần tử
- generator là cách tạo iterator gọn hơn

### Mức độ quan trọng
**Quan trọng về tư duy**

---

## 10. `10_modules_and_packages.py`
### Nội dung
- `import`
- `from ... import ...`
- alias (`as`)
- module built-in
- module tự tạo
- package

### Cần nhớ
- module = file `.py`
- package = thư mục chứa nhiều module
- dùng import để tách code sang nhiều file

### Mức độ quan trọng
**Rất quan trọng**

---

## 11. `11_dates_math.py`
### Nội dung
- module `math`
- module `datetime`
- `strftime()`
- `strptime()`
- `timedelta`

### Cần nhớ
- `datetime.now()` lấy thời gian hiện tại
- `strftime()` format ngày thành chuỗi
- `strptime()` parse chuỗi thành ngày
- `timedelta` để cộng/trừ thời gian

### Mức độ quan trọng
**Quan trọng thực dụng**

---

## 12. `12_json.py`
### Nội dung
- JSON là gì
- `json.dumps()` / `json.loads()`
- `json.dump()` / `json.load()`
- đọc ghi JSON từ file

### Cần nhớ
- `dumps/loads` làm việc với string
- `dump/load` làm việc với file
- JSON cực quan trọng với API/backend

### Mức độ quan trọng
**Cực kỳ quan trọng**

---

## 13. `13_regex.py`
### Nội dung
- `re.search()`
- `re.match()`
- `re.findall()`
- `re.finditer()`
- `re.split()`
- `re.sub()`
- metacharacters
- special sequences
- group
- `re.compile()`
- flags

### Cần nhớ
- regex dùng để tìm, tách, thay thế chuỗi theo mẫu
- các pattern cơ bản như `\d`, `\w`, `\s`, `[]`, `+`, `*`, `?`
- regex mạnh nhưng dễ rối nếu lạm dụng

### Mức độ quan trọng
**Quan trọng**

---

## 14. `14_strings.py`
### Nội dung
- tạo chuỗi
- nối chuỗi
- slicing
- duyệt chuỗi
- string methods
- `split()` / `join()`
- format string
- escape characters
- `isalpha()`, `isdigit()`, `isalnum()`, ...
- đảo chuỗi bằng slicing

### Cần nhớ
- `strip()`, `replace()`, `split()`, `join()` là bộ rất hay dùng
- f-string là cách format hiện đại và rõ ràng
- slicing string cực quan trọng

### Mức độ quan trọng
**Cực kỳ quan trọng**

---

## 15. `15_virtualenv_pip.py`
### Nội dung
- pip
- cài, gỡ package
- `requirements.txt`
- `venv`
- activate / deactivate
- kiểm tra môi trường hiện tại

### Cần nhớ
- luôn dùng virtualenv cho project
- không cài lung tung vào global environment
- `pip freeze > requirements.txt`
- `pip install -r requirements.txt`

### Mức độ quan trọng
**Rất quan trọng**

---

## 16. `16_exceptions.py`
### Nội dung
- các loại exception phổ biến
- `try / except / else / finally`
- traceback
- `raise`
- custom exceptions
- exception chaining
- `assert`

### Cần nhớ
- phải biết bắt lỗi đúng loại
- `raise` để chủ động báo lỗi
- `finally` luôn chạy
- không nên lạm dụng `except Exception`

### Mức độ quan trọng
**Cực kỳ quan trọng**

---

## 17. `17_file_io.py`
### Nội dung
- `pathlib`
- tạo và xử lý path
- đọc/ghi file text
- `seek()` / `tell()`
- `read_text()` / `write_text()`
- copy, move, rename, delete file
- các mode file như `a`, `x`, `b`

### Cần nhớ
- `with open(...)` là cách chuẩn để làm việc với file
- nhớ `encoding="utf-8"`
- `pathlib` tiện và hiện đại hơn `os.path`

### Mức độ quan trọng
**Cực kỳ quan trọng**

---

## 18. `18_list_comprehension.py`
### Nội dung
- list comprehension
- dict comprehension
- set comprehension
- `enumerate()`
- `zip()`
- ternary operator
- unpacking
- merge dict bằng `|`

### Cần nhớ
- comprehension giúp code gọn hơn
- `enumerate()` dùng khi cần index + value
- `zip()` dùng để duyệt song song nhiều list
- unpacking giúp viết code Pythonic hơn

### Mức độ quan trọng
**Rất quan trọng**

---

## 19. `19_typing.py`
### Nội dung
- type hints cho biến và hàm
- `List`, `Dict`, `Tuple`
- `Optional`, `Union`, `Any`
- class type hints
- type alias

### Cần nhớ
- type hints giúp code rõ hơn, IDE hỗ trợ tốt hơn
- type hints không ép runtime mặc định
- nên annotate function input/output

### Mức độ quan trọng
**Quan trọng**

---

# PHÂN LOẠI THEO MỨC ĐỘ ƯU TIÊN

## Nhóm bắt buộc phải rất chắc
- 1. Biến và kiểu dữ liệu
- 2. Toán tử
- 3. Collections
- 4. Điều kiện
- 5. Vòng lặp
- 6. Hàm
- 12. JSON
- 14. String
- 16. Exceptions
- 17. File I/O

## Nhóm rất nên biết tốt
- 7. Range
- 8. List methods
- 10. Modules & packages
- 11. Datetime / math
- 15. Pip / virtualenv
- 18. Comprehensions / enumerate / zip
- 19. Typing

## Nhóm nên hiểu để mở rộng tư duy
- 9. Iterator
- 13. Regex nâng cao
- Decorator trong file 6

---

# HỌC XONG BỘ NÀY ANH SẼ CÓ GÌ?

Nếu học kỹ và làm bài tập đủ, anh sẽ:
- đọc hiểu Python cơ bản ổn
- xử lý được list / dict / string / file / json
- viết function tử tế hơn
- biết debug lỗi cơ bản
- có nền tốt để học OOP
- sẵn sàng bước sang project nhỏ hoặc FastAPI cơ bản

---

# BỘ NÀY CÒN THIẾU GÌ?

Để đi tiếp sang project thực tế, cần bổ sung:
- OOP Pythonic
- project structure
- pytest / testing
- framework (nếu đi backend thì là FastAPI)
- logging / clean code tools

---

# KẾT LUẬN

Bộ tài liệu này là **nền Python base khá ổn**.
Nó đủ tốt để:
- ôn Python nhanh
- chuyển từ stack khác sang Python
- làm bàn đạp để học OOP và framework

Nhưng muốn làm project sạch và thực chiến hơn thì sau bộ này cần học tiếp:
- OOP
- testing
- framework
- cách tổ chức project
