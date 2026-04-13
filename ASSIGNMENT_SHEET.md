# PYTHON BASE — ASSIGNMENT SHEET

Mục tiêu: ôn tổng quát Python base để chuyển sang OOP.

## Rules
- Không copy từ note khi đang làm bài
- Mỗi bài ưu tiên viết thành function
- Tự test ít nhất 2-3 case
- Nếu bí: xem lại concept, không xem đáp án full

---

## Level 1 — Warm-up

### Bài 1 — Normalize Name
**Đề bài:**
Viết hàm `normalize_name(name)` để:
- bỏ khoảng trắng thừa đầu/cuối
- nhiều space giữa các từ -> 1 space
- viết hoa chữ cái đầu mỗi từ

**Ví dụ:**
```python
"   nGuYEn   van   a  " -> "Nguyen Van A"
```

**Ôn:** string, `strip`, `split`, `join`, `title`
**Độ khó:** Easy

---

### Bài 2 — Even / Odd Summary
**Đề bài:**
Cho list số:
```python
nums = [1,2,3,4,5,6,7,8,9,10]
```
Viết hàm trả về:
- danh sách số chẵn
- danh sách số lẻ
- tổng số chẵn
- tổng số lẻ

**Ôn:** loop, if, list, function
**Độ khó:** Easy

---

### Bài 3 — Score Statistics
**Đề bài:**
Cho:
```python
scores = [8, 5, 9, 4, 7, 10, 6, 5, 8]
```
Trả về dict:
```python
{
    "avg": ...,
    "max": ...,
    "min": ...,
    "gioi": ...,
    "kha": ...,
    "yeu": ...
}
```
Quy ước:
- `gioi >= 8`
- `kha = 6 hoặc 7`
- `yeu < 6`

**Ôn:** list, dict, condition, built-in
**Độ khó:** Easy-Medium

---

### Bài 4 — Count Characters
**Đề bài:**
Viết hàm `count_chars(text)` đếm số lần xuất hiện của từng ký tự.

**Ví dụ:**
```python
"banana" -> {"b": 1, "a": 3, "n": 2}
```

**Ôn:** dict, loop, string
**Độ khó:** Easy-Medium

---

### Bài 5 — Remove Duplicates
**Đề bài:**
Viết hàm `remove_duplicates(nums)`:
- giữ nguyên thứ tự xuất hiện đầu tiên
- bỏ phần tử trùng

**Ví dụ:**
```python
[1, 2, 2, 3, 1, 4] -> [1, 2, 3, 4]
```

**Ôn:** list, set, membership
**Độ khó:** Medium

---

## Level 2 — Functions + Processing

### Bài 6 — Analyze Numbers
**Đề bài:**
Viết hàm `analyze_numbers(nums)` trả về:
- `sum`
- `avg`
- `max`
- `min`
- `even_count`
- `odd_count`
- `unique_sorted`

**Ôn:** function, loop, built-in, sorting
**Độ khó:** Medium

---

### Bài 7 — Multiplication Table
**Đề bài:**
- In bảng cửu chương từ 2 đến 9
- Bonus: viết hàm `print_table(n)` để in riêng bảng `n`

**Ôn:** nested loop, range
**Độ khó:** Medium

---

### Bài 8 — Prime Numbers in Range
**Đề bài:**
Viết hàm `primes_in_range(start, end)` trả về các số nguyên tố trong đoạn.

**Ôn:** function, loop, condition
**Độ khó:** Medium

---

### Bài 9 — Factorial & Fibonacci
**Đề bài:**
Viết:
- `factorial(n)`
- `fibonacci(n)` trả về `n` số đầu tiên

Làm 2 cách nếu được:
- dùng loop
- dùng recursion

**Ôn:** function, recursion
**Độ khó:** Medium

---

## Level 3 — String / Dict / List tổng hợp

### Bài 10 — Word Count
**Đề bài:**
Viết hàm `word_count(sentence)`:
- tách từ
- không phân biệt hoa thường
- đếm số lần xuất hiện từng từ

**Ví dụ:**
```python
"Python python Java" -> {"python": 2, "java": 1}
```

**Ôn:** string, dict, `split`, `lower`
**Độ khó:** Medium

---

### Bài 11 — Filter Valid Emails
**Đề bài:**
Cho:
```python
emails = ["a@gmail.com", "abc", "test@yahoo.com", "x@x", "hello@company.vn"]
```
Viết hàm lọc email hợp lệ đơn giản nếu:
- có `@`
- có dấu `.` sau `@`

**Bonus:** dùng regex

**Ôn:** string methods, condition, regex
**Độ khó:** Medium

---

### Bài 12 — Group Students by Result
**Đề bài:**
Cho:
```python
students = [
    {"name": "An", "score": 8},
    {"name": "Binh", "score": 5},
    {"name": "Chi", "score": 7},
    {"name": "Dung", "score": 9}
]
```
Trả về:
```python
{
    "passed": [...],
    "failed": [...]
}
```
Đậu nếu `score >= 6`

**Ôn:** list of dict, condition, append
**Độ khó:** Medium

---

## Level 4 — File / JSON / Exception

### Bài 13 — File Summary
**Đề bài:**
Tạo file text bất kỳ, viết script:
- đọc file
- đếm số dòng
- đếm số từ
- đếm số ký tự

**Ôn:** file I/O, string processing
**Độ khó:** Medium

---

### Bài 14 — JSON Report
**Đề bài:**
Cho file `students.json`:
```json
[
  {"name": "An", "score": 8},
  {"name": "Binh", "score": 5},
  {"name": "Chi", "score": 9}
]
```
Viết script:
- đọc JSON
- tính điểm trung bình
- tạo `report.json`

**Output mẫu:**
```json
{
  "avg": 7.33,
  "passed": ["An", "Chi"],
  "failed": ["Binh"]
}
```

**Ôn:** json, file, loop, dict/list
**Độ khó:** Medium-Hard

---

### Bài 15 — Safe Divide
**Đề bài:**
Viết hàm `safe_divide(a, b)`:
- nếu `b == 0` -> raise `ValueError`
- nếu input không phải số -> raise `TypeError`
- dùng `try/except` bên ngoài để xử lý đẹp

**Ôn:** exceptions, raise, validation
**Độ khó:** Medium

---

### Bài 16 — Input Validation Loop
**Đề bài:**
Viết chương trình:
- yêu cầu user nhập tuổi
- nếu nhập sai thì báo lỗi và nhập lại
- chỉ dừng khi nhập đúng số nguyên dương

**Ôn:** `while`, `try/except`, input, validation
**Độ khó:** Medium

---

## Level 5 — Modules / Comprehension / Typing

### Bài 17 — Split into Modules
**Đề bài:**
Tạo:
- `math_utils.py`
- `main.py`

Trong `math_utils.py` viết:
- `is_prime`
- `factorial`
- `sum_even`

`main.py` import và gọi thử.

**Ôn:** modules, import
**Độ khó:** Medium

---

### Bài 18 — Rewrite with Comprehension
**Đề bài:**
Cho:
```python
nums = [1, 2, 3, 4, 5, 6]
```
Làm các yêu cầu:
- list bình phương
- list số chẵn
- dict `{n: n*n}`
- set bình phương không trùng

**Ôn:** list/dict/set comprehension
**Độ khó:** Medium

---

### Bài 19 — Enumerate & Zip
**Đề bài:**
Cho:
```python
names = ["An", "Binh", "Chi"]
scores = [8, 9, 7]
```
Yêu cầu:
- in ra STT + tên
- ghép tên với điểm
- tạo dict `{name: score}`

**Ôn:** `enumerate`, `zip`, dict
**Độ khó:** Easy-Medium

---

### Bài 20 — Add Type Hints
**Đề bài:**
Lấy 3 hàm cũ anh đã viết, thêm type hints cho:
- parameter
- return type

**Ví dụ:**
```python
def normalize_name(name: str) -> str:
```

**Ôn:** typing cơ bản
**Độ khó:** Easy-Medium

---

## Level 6 — Final Bridge to OOP

### Bài 21 — Student Manager (Function-based)
**Đề bài:**
Viết chương trình quản lý sinh viên bằng **list of dict**, chưa dùng class.

Mỗi sinh viên có dạng:
```python
{
    "id": int,
    "name": str,
    "score": float
}
```

Viết các hàm:
- `add_student`
- `find_student_by_id`
- `update_score`
- `delete_student`
- `sort_by_score`
- `save_to_json`
- `load_from_json`

**Ôn tổng hợp:**
- function
- list/dict
- file/json
- exception
- module hóa nếu muốn

**Ý nghĩa:**
Đây là bài cầu nối sang OOP. Làm xong bài này, anh sẽ thấy rất rõ vì sao cần class/object.

**Độ khó:** Hard

---

## Recommended Order (nếu ôn nhanh)

### Bắt buộc làm
- Bài 1
- Bài 3
- Bài 6
- Bài 10
- Bài 14
- Bài 15
- Bài 18
- Bài 21

### Nên làm thêm
- Bài 5
- Bài 8
- Bài 12
- Bài 16
- Bài 19
- Bài 20

---

## Pass Criteria để chuyển sang OOP
- Tự viết function không quá lúng túng
- Xử lý `list` / `dict` / `string` ổn
- Đọc ghi JSON không nhầm
- Biết validate input
- Biết dùng `try/except`
- Làm bài 21 mà bắt đầu thấy function-based approach hơi rối

Nếu tới bài 21 mà anh thấy code bắt đầu phình ra và khó quản lý, đó chính là thời điểm đẹp nhất để chuyển sang OOP.
