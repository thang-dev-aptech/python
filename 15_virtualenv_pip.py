# ============================================================
# PYTHON CHEATSHEET - PHẦN 15: VIRTUALENV & PIP
# ============================================================

# Giới thiệu:
# - PIP: Trình quản lý gói chuẩn của Python (Package Installer for Python).
# - Virtual Environment (Môi trường ảo): Cho phép tạo các không gian làm việc
#   độc lập cho từng dự án, tránh xung đột phiên bản thư viện giữa các dự án.

# ============================================================
# 1. QUẢN LÝ GÓI VỚI PIP (Package Installer for Python)
# ============================================================
# Lưu ý: Các lệnh này chạy trong TERMINAL (CMD/PowerShell/Terminal),
# không chạy trực tiếp trong code Python.

# 1.1. Các lệnh cơ bản
# Kiểm tra phiên bản pip hiện tại
#   pip --version

# Cài đặt một thư viện (ví dụ: requests)
#   pip install requests

# Cài đặt phiên bản cụ thể (rất quan trọng để đảm bảo tính tương thích)
#   pip install requests==2.31.0
#   pip install "requests>=2.0,<3.0"

# Nâng cấp thư viện lên bản mới nhất
#   pip install --upgrade requests

# Gỡ bỏ thư viện
#   pip uninstall requests
#   (Thêm -y để không cần xác nhận: pip uninstall -y requests)

# 1.2. Quản lý danh sách thư viện
# Liệt kê các thư viện đã cài trong môi trường hiện tại
#   pip list

# Xem thông tin chi tiết về một thư viện (phiên bản, tác giả, nơi cài đặt...)
#   pip show requests

# Kiểm tra các thư viện bị xung đột dependencies
#   pip check

# 1.3. Quản lý Dependencies cho dự án (requirements.txt)
# Xuất danh sách tất cả thư viện hiện có ra file requirements.txt
# (Thường làm khi chia sẻ dự án hoặc deploy)
#   pip freeze > requirements.txt

# Cài đặt toàn bộ thư viện từ file requirements.txt
#   pip install -r requirements.txt

# ============================================================
# 2. VIRTUAL ENVIRONMENT (MÔI TRƯỜNG ẢO - venv)
# ============================================================
# Tại sao cần venv?
# - Dự án A dùng thư viện X v1.0, Dự án B dùng thư viện X v2.0.
# - Nếu cài vào môi trường toàn cục (Global), sẽ bị xung đột.
# -> venv giúp mỗi dự án có một bộ thư viện riêng biệt.

# 2.1. Tạo môi trường ảo
# (Python 3.3+ đã tích hợp module `venv`)
# Chạy lệnh sau tại thư mục gốc của dự án:
#   python -m venv venv
# (Lưu ý: tham số cuối là tên thư mục, thường đặt là `venv`, `.venv` hoặc `env`)

# 2.2. Kích hoạt môi trường ảo (Activate)
# Sau khi kích hoạt, tên môi trường sẽ hiện phía trước dấu nhắc lệnh, vd: (venv)

# --- Trên Windows ---
# Command Prompt (cmd):
#   venv\Scripts\activate
# PowerShell:
#   venv\Scripts\Activate.ps1
# (Nếu lỗi quyền thực thi script, chạy: Set-ExecutionPolicy Unrestricted -Scope Process)

# --- Trên macOS / Linux ---
#   source venv/bin/activate

# 2.3. Kiểm tra sau khi kích hoạt
# Gõ `which python` (macOS/Linux) hoặc `where python` (Windows)
# để đảm bảo nó đang trỏ vào thư mục venv/bin/python hoặc venv\Scripts\python.exe

# 2.4. Hủy kích hoạt (Deactivate)
# Khi làm xong hoặc muốn chuyển dự án khác:
#   deactivate

# 2.5. Xóa môi trường ảo
# Chỉ cần xóa thư mục `venv` đi là xong.
#   Windows: rmdir /s /q venv
#   Mac/Linux: rm -rf venv

# ============================================================
# 3. BEST PRACTICES (THỰC HÀNH TỐT NHẤT)
# ============================================================
# 1. Luôn sử dụng virtualenv cho mọi dự án Python quan trọng.
# 2. Thêm tên thư mục môi trường ảo (vd: `venv/`, `.env/`) vào file `.gitignore`
#    để không đẩy hàng nghìn file thư viện lên Git.
# 3. Luôn tạo file `requirements.txt` để người khác dễ dàng cài đặt lại môi trường.
# 4. Đừng cài đặt lung tung vào môi trường Global hệ thống (nhất là trên Mac/Linux)
#    để tránh lỗi hệ điều hành.

# ============================================================
# 4. VÍ DỤ MINH HỌA TRONG CODE (Kiểm tra môi trường)
# ============================================================
import sys

def check_environment():
    print("Thông tin môi trường Python đang chạy:")
    print(f"- Đường dẫn Python executable: {sys.executable}")
    print(f"- Phiên bản Python: {sys.version}")
    
    # Kiểm tra xem có đang chạy trong môi trường ảo không
    # (Cách nhận biết cơ bản: sys.base_prefix khác sys.prefix)
    is_venv = (sys.prefix != sys.base_prefix)
    if is_venv:
        print("-> ĐANG CHẠY TRONG VIRTUAL ENVIRONMENT.")
    else:
        print("-> Đang chạy trong môi trường GLOBAL (Hệ thống).")

if __name__ == "__main__":
    check_environment()
