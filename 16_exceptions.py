# ============================================================
# PYTHON CHEATSHEET - PHẦN 16: EXCEPTIONS (XỬ LÝ NGOẠI LỆ)
# ============================================================

import sys
import traceback

# ============================================================
# 1. CÁC LOẠI LỖI THƯỜNG GẶP (BUILT-IN EXCEPTIONS)
# ============================================================
# - SyntaxError: Lỗi cú pháp (code sai quy tắc).
# - IndentationError: Lỗi thụt đầu dòng.
# - NameError: Dùng biến chưa được định nghĩa.
# - TypeError: Phép toán không hợp lệ trên kiểu dữ liệu (vd: "abc" + 1).
# - ValueError: Giá trị không hợp lệ (vd: int("abc")).
# - ZeroDivisionError: Chia cho 0.
# - IndexError: Truy cập chỉ số không tồn tại trong list/tuple.
# - KeyError: Truy cập key không tồn tại trong dict.
# - FileNotFoundError: Mở file không tồn tại.
# - AttributeError: Gọi thuộc tính/phương thức không có trong object.

# ============================================================
# 2. CẤU TRÚC TRY - EXCEPT - ELSE - FINALLY
# ============================================================
print("\n--- 2. Try - Except - Else - Finally ---")

def divide_numbers(a, b):
    try:
        # Khối code có thể gây ra lỗi
        result = a / b
    except ZeroDivisionError:
        # Chạy khi gặp lỗi chia cho 0
        print("Lỗi: Không thể chia cho 0!")
        result = None
    except TypeError:
        # Chạy khi kiểu dữ liệu không đúng
        print("Lỗi: Kiểu dữ liệu không hợp lệ!")
        result = None
    except Exception as e:
        # Bắt tất cả các lỗi khác (nên hạn chế dùng nếu không cần thiết)
        print(f"Lỗi không xác định: {e}")
        result = None
    else:
        # Chạy khi KHÔNG có lỗi xảy ra trong khối try
        print(f"Kết quả phép chia: {result}")
    finally:
        # LUÔN LUÔN chạy, dù có lỗi hay không (thường dùng để dọn dẹp, đóng file, ngắt kết nối DB)
        print("-> Đã thực hiện xong khối lệnh chia.")
    return result

divide_numbers(10, 2)  # Thành công
divide_numbers(10, 0)  # Lỗi ZeroDivisionError
divide_numbers(10, "a") # Lỗi TypeError

# ============================================================
# 3. LẤY THÔNG TIN CHI TIẾT VỀ LỖI (TRACEBACK & SYS)
# ============================================================
print("\n--- 3. Traceback & Sys ---")

try:
    x = int("invalid")
except ValueError:
    # Cách 1: In lỗi đơn giản
    print("Caught ValueError.")
    
    # Cách 2: Lấy thông tin chi tiết từ sys.exc_info()
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print(f"Loại lỗi: {exc_type.__name__}")
    print(f"Nội dung: {exc_value}")

    # Cách 3: In đầy đủ stack trace (giống như Python in mặc định khi crash)
    print("Stack trace đầy đủ:")
    traceback.print_exc()

# ============================================================
# 4. RAISE - CHỦ ĐỘNG NÉM RA LỖI
# ============================================================
print("\n--- 4. Raise Exception ---")

def validate_age(age):
    if age < 0:
        # Chủ động báo lỗi ValueError
        raise ValueError("Tuổi không thể là số âm!")
    if age < 18:
        print("Bạn chưa đủ tuổi.")
    else:
        print("Bạn đủ tuổi.")

try:
    validate_age(-5)
except ValueError as e:
    print(f"Bắt được lỗi: {e}")

# Exception Chaining (raise ... from ...)
# Dùng để gói một lỗi này trong một lỗi khác, giữ lại ngữ cảnh của lỗi gốc
try:
    try:
        val = int("not_a_number")
    except ValueError as e:
        # Ném ra RuntimeError nhưng vẫn giữ nguyên nhân gốc là ValueError
        raise RuntimeError("Lỗi nghiêm trọng khi xử lý dữ liệu") from e
except RuntimeError as e:
    print(f"\nChained Exception Catch: {e}")
    print(f"Nguyên nhân gốc (Cause): {e.__cause__}")

# ============================================================
# 5. CUSTOM EXCEPTIONS (TỰ ĐỊNH NGHĨA LỖI)
# ============================================================
print("\n--- 5. Custom Exceptions ---")

class PaymentError(Exception):
    """Lỗi chung cho thanh toán"""
    pass

class InsufficientFundsError(PaymentError):
    """Lỗi không đủ tiền"""
    def __init__(self, amount, balance):
        self.amount = amount
        self.balance = balance
        super().__init__(f"Không đủ tiền: Cần {amount}, chỉ có {balance}")

try:
    balance = 100
    amount = 500
    if amount > balance:
        raise InsufficientFundsError(amount, balance)
except InsufficientFundsError as e:
    print(f"Giao dịch thất bại: {e}")

# ============================================================
# 6. ASSERT (KHẲNG ĐỊNH)
# ============================================================
# Dùng để debug, kiểm tra điều kiện phải luôn đúng. 
# Nếu sai sẽ ném ra AssertionError.
# Lưu ý: assert có thể bị vô hiệu hóa khi chạy python với flag -O (optimize).

x = 100
# assert x < 0, "x phải là số âm"  # Dòng này sẽ gây lỗi AssertionError nếu chạy
