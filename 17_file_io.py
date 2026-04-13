# ============================================================
# PYTHON CHEATSHEET - PHẦN 17: FILE I/O THE NEW WAY
# ============================================================

import os
import shutil
from pathlib import Path

# ============================================================
# 1. PATHLIB - XỬ LÝ ĐƯỜNG DẪN HIỆN ĐẠI (Nên dùng thay os.path)
# ============================================================
print("--- 1. Pathlib Basics ---")

# Đường dẫn hiện tại
current_dir = Path.cwd()
print(f"Thư mục hiện tại: {current_dir}")

# Tạo đường dẫn file (tương thích cả Windows/Mac/Linux)
file_path = current_dir / "example_data" / "demo.txt"
print(f"Đường dẫn file: {file_path}")

# Tạo thư mục (nếu chưa có)
# parents=True: tạo cả thư mục cha nếu cần
# exist_ok=True: không báo lỗi nếu thư mục đã tồn tại
(current_dir / "example_data").mkdir(parents=True, exist_ok=True)

# ============================================================
# 2. ĐỌC VÀ GHI FILE CƠ BẢN (TEXT)
# ============================================================
print("\n--- 2. Read/Write Text ---")

# Ghi file (Write)
# mode 'w': Ghi mới (xóa nội dung cũ). encoding='utf-8' quan trọng cho tiếng Việt.
with open(file_path, mode="w", encoding="utf-8") as f:
    f.write("Dòng 1: Hello Python.\n")
    f.write("Dòng 2: Xin chào Việt Nam.\n")
    f.writelines(["Dòng 3: List line A.\n", "Dòng 4: List line B.\n"])

print(f"Đã ghi vào: {file_path.name}")

# Đọc file (Read)
# mode 'r': Đọc (mặc định)
with open(file_path, mode="r", encoding="utf-8") as f:
    content = f.read()
    print("--- Nội dung file ---")
    print(content)

# Đọc từng dòng (cho file lớn để tiết kiệm RAM)
print("--- Đọc từng dòng ---")
with open(file_path, mode="r", encoding="utf-8") as f:
    for i, line in enumerate(f, 1):
        print(f"Line {i}: {line.strip()}")

# ============================================================
# 3. CON TRỎ FILE (SEEK & TELL)
# ============================================================
print("\n--- 3. Seek & Tell ---")
with open(file_path, "r", encoding="utf-8") as f:
    print(f"Vị trí đầu: {f.tell()}")
    f.read(7) # Đọc 7 ký tự
    print(f"Đọc 7 ký tự. Vị trí hiện tại: {f.tell()}")
    
    f.seek(0) # Quay về đầu file
    print(f"Seek(0). Vị trí hiện tại: {f.tell()}")
    print(f"Đọc lại từ đầu: {f.read(5)}...")

# ============================================================
# 4. PATHLIB SHORTCUTS (Rất tiện lợi)
# ============================================================
# Pathlib có sẵn hàm read/write text/bytes nhanh mà không cần with open
# Lưu ý: Chỉ dùng cho file nhỏ, không dùng cho file GB.

path_quick = current_dir / "quick_note.txt"
path_quick.write_text("Nội dung tạo nhanh bằng pathlib.", encoding="utf-8")
print(f"\nĐọc nhanh pathlib: {path_quick.read_text(encoding='utf-8')}")
path_quick.unlink() # Xóa file

# ============================================================
# 5. QUẢN LÝ FILE & THƯ MỤC (OS & SHUTIL)
# ============================================================
# Pathlib làm được nhiều việc, nhưng shutil mạnh hơn về copy/move.

src = file_path
dst = current_dir / "example_data" / "demo_copy.txt"

# Copy file
shutil.copy2(src, dst) # copy2 giữ nguyên metadata (ngày tạo...)
print(f"\nĐã copy {src.name} -> {dst.name}")

# Đổi tên / Di chuyển (Rename / Move)
moved_path = current_dir / "example_data" / "demo_renamed.txt"
if dst.exists():
    os.rename(dst, moved_path) # Hoặc dùng shutil.move(dst, moved_path)
    print(f"Đã đổi tên {dst.name} -> {moved_path.name}")

# Kiểm tra tồn tại
if moved_path.exists():
    print(f"{moved_path.name} có tồn tại? {moved_path.exists()}")
    print(f"Là file? {moved_path.is_file()}")
    print(f"Là thư mục? {moved_path.is_dir()}")

# Xóa file
try:
    moved_path.unlink() # Xóa file
    print("Đã xóa file renamed.")
    # (current_dir / "example_data" / "demo.txt").unlink() # Xóa file gốc nếu muốn
except FileNotFoundError:
    pass

# Xóa thư mục (Cẩn thận!)
# dir_to_delete = current_dir / "example_data"
# if dir_to_delete.exists():
#     shutil.rmtree(dir_to_delete) # Xóa thư mục và toàn bộ nội dung bên trong
#     print("Đã xóa thư mục example_data.")

# ============================================================
# 6. CÁC MODE FILE KHÁC
# ============================================================
# 'a' (Append): Ghi nối tiếp vào cuối file
# 'x' (Exclusive creation): Tạo file mới, nếu file đã tồn tại sẽ báo lỗi (tránh ghi đè nhầm)
# 'b' (Binary): Dùng cho ảnh, video, pdf... (vd: 'rb', 'wb')

# Ví dụ Append
with open(file_path, "a", encoding="utf-8") as f:
    f.write("Dòng 5: Ghi thêm bằng mode append.\n")

print("\nĐã append thêm vào file demo.txt")
