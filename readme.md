# Python Learning Roadmap (Base ➜ Nâng cao)

Bộ file hiện tại (`1_...` đến `19_...`) là phần **base** để nắm cú pháp và tư duy nền tảng.
Mục tiêu của README này: sau khi học xong base, anh có ngay lộ trình học tiếp để lên mức làm project thực tế.

---

## 0) Cách học bộ base hiện tại

- Học theo thứ tự file số (`1 -> 19`)
- Mỗi file nên làm 3 bước:
  1. Đọc + chạy lại ví dụ
  2. Tự sửa ví dụ thành bài toán riêng
  3. Ghi lại 3 ý chính vào note cá nhân
- Sau mỗi 3 file: làm 1 mini bài tập tổng hợp

> Mục tiêu pass base: đọc code Python cơ bản không bị ngợp, tự viết script nhỏ, tự debug lỗi cơ bản.

---

## 1) Những phần cần bổ sung sau khi xong base

## A. OOP Pythonic (rất quan trọng)

Hiện base có nhắc khái niệm nhưng cần học sâu thêm:
- `class`, `__init__`, instance/class attributes
- `@dataclass`
- Inheritance vs Composition
- `@property`, `@classmethod`, `@staticmethod`
- Dunder methods: `__repr__`, `__str__`, `__eq__`

**Output cần đạt:**
- Tự thiết kế class cho 1 domain nhỏ (VD: Student/Course/Enrollment)
- Viết object model rõ ràng, đặt tên tốt, tránh code lặp

---

## B. Pythonic tools & standard library

- `collections`: `Counter`, `defaultdict`, `deque`
- `itertools`: `chain`, `groupby`, `product`
- `functools`: `lru_cache`, `partial`
- `pathlib` nâng cao
- `datetime` + timezone cơ bản

**Output cần đạt:**
- Biết chọn đúng tool thay vì tự code vòng lặp dài dòng

---

## C. Testing + code quality (để code “dùng được”)

- `pytest` cơ bản + test edge cases
- `black` (format), `ruff` (lint), `mypy` (type check)
- Logging (`logging`) thay cho `print()` khi làm project

**Output cần đạt:**
- Viết được test cho business logic
- Chạy được bộ check trước khi commit

---

## D. Project structure & packaging

- Cấu trúc project Python rõ ràng:
  - `app/`, `tests/`, `scripts/`
- Quản lý dependency với `venv` + `requirements.txt`
- Nâng cấp dần sang `pyproject.toml`
- Tách config theo môi trường (`.env`, dev/prod)

**Output cần đạt:**
- Tạo được repo sạch, chạy được ở máy khác bằng vài lệnh

---

## E. FastAPI thực chiến (đúng mục tiêu README cũ)

Thứ tự đề xuất:
1. FastAPI basics (router, request/response)
2. Pydantic models (validation)
3. CRUD API + error handling
4. DB integration (SQLAlchemy hoặc Mongo)
5. Auth cơ bản (JWT)
6. Pagination/filter/sort
7. API docs + test API

**Output cần đạt:**
- 1 API project hoàn chỉnh có test cơ bản

---

## 2) Lộ trình 4 tuần sau base (gợi ý)

### Tuần 1: OOP Pythonic + standard library
- Ngày 1-2: class/dataclass
- Ngày 3: dunder methods/property
- Ngày 4: collections/itertools
- Ngày 5: mini project CLI nhỏ

### Tuần 2: Testing + clean code
- Ngày 1-2: pytest cơ bản
- Ngày 3: edge cases + mock cơ bản
- Ngày 4: ruff/black/mypy
- Ngày 5: refactor mini project + thêm test

### Tuần 3: FastAPI cơ bản
- Router, schema, validation, CRUD in-memory
- Chuyển qua DB thật vào cuối tuần

### Tuần 4: FastAPI nâng cao + deploy mindset
- Auth, phân tầng service/repository
- Docker cơ bản + `.env`
- Viết README project + cách chạy

---

## 3) Checklist hoàn thành mức “nắm chắc Python cơ bản nâng cao”

- [ ] Tự viết script xử lý file/json + exception sạch
- [ ] Tự thiết kế class model hợp lý
- [ ] Có thói quen viết test cho logic quan trọng
- [ ] Dùng lint/format/type-check trước commit
- [ ] Build được 1 FastAPI CRUD có DB + auth cơ bản
- [ ] Giải thích được code của mình (không copy mù)

---

## 4) Gợi ý mini project sau khi học xong base

1. **Student Manager CLI**
   - OOP + file/json + exception + typing
2. **Expense Tracker API**
   - FastAPI + CRUD + validation + DB
3. **Log Analyzer**
   - regex + file I/O + collections + test

---

## 5) Note kỹ thuật quan trọng

- Tránh đặt tên biến trùng built-in: `list`, `dict`, `sum`, `str`, ...
- Luôn dùng virtualenv cho mỗi project
- Ưu tiên code rõ ràng trước, tối ưu sau
- Học đến đâu làm project đến đó

---

Nếu cần, có thể tạo thêm file `ROADMAP_30_DAYS.md` với plan theo **từng ngày** (task + output + tiêu chí pass).