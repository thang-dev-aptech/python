import re

# RegEx (Regular Expression) là một chuỗi các ký tự tạo thành một mẫu tìm kiếm.
# Được sử dụng để kiểm tra xem một chuỗi có chứa mẫu tìm kiếm cụ thể hay không.

text = "Hôm nay là ngày 12/01/2026. Nhiệt độ là 25 độ C. Liên hệ: admin@example.com hoặc support@test.vn"

# --- 1. Các hàm cơ bản trong module re ---

# re.search(): Quét toàn bộ chuỗi để tìm vị trí khớp ĐẦU TIÊN.
# Trả về đối tượng Match nếu tìm thấy, nếu không trả về None.
match = re.search(r"\d{2}/\d{2}/\d{4}", text)
if match:
    # .group() trả về phần chuỗi khớp
    # .span() trả về tuple (start, end)
    print(f"1. Tìm thấy ngày tháng (search): {match.group()} tại vị trí {match.span()}")
else:
    print("1. Không tìm thấy ngày tháng")

# re.match(): Chỉ kiểm tra khớp ở NGAY ĐẦU chuỗi.
match_at_start = re.match(r"Hôm nay", text)
if match_at_start:
    print(f"2. Tìm thấy ở đầu chuỗi (match): {match_at_start.group()}")
else:
    print("2. Không tìm thấy ở đầu chuỗi")

# re.findall(): Trả về DANH SÁCH chứa tất cả các chuỗi con trùng khớp.
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)
print(f"3. Danh sách email tìm thấy (findall): {emails}")

# re.finditer(): Giống findall nhưng trả về một iterator chứa các đối tượng Match.
print("4. Duyệt qua kết quả (finditer):")
for m in re.finditer(r"\d+", text):
    print(f"   - Tìm thấy số '{m.group()}' tại {m.span()}")

# re.split(): Tách chuỗi tại mỗi lần xuất hiện của mẫu.
# Tách câu dựa trên dấu chấm hoặc dấu chấm than/hỏi
sentence = "Xin chào. Bạn khỏe không? Tôi rất vui."
parts = re.split(r"[.?!]\s*", sentence)
# Lọc bỏ phần tử rỗng nếu có
parts = [p for p in parts if p]
print(f"5. Tách chuỗi (split): {parts}")

# re.sub(): Thay thế một hoặc nhiều lần xuất hiện của mẫu bằng chuỗi khác.
# Ví dụ: Ẩn số điện thoại hoặc email
masked_text = re.sub(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}", "[EMAIL HIDDEN]", text)
print(f"6. Thay thế (sub): {masked_text}")


# --- 2. Metacharacters (Ký tự đặc biệt) ---
# [] : Tập hợp các ký tự. Vd: "[a-m]" (từ a đến m)
# \  : Escape character (để tìm ký tự đặc biệt như \. hay \*) hoặc bắt đầu sequence (\d)
# .  : Bất kỳ ký tự nào (trừ dòng mới)
# ^  : Bắt đầu chuỗi
# $  : Kết thúc chuỗi
# *  : 0 hoặc nhiều lần
# +  : 1 hoặc nhiều lần
# ?  : 0 hoặc 1 lần (hoặc non-greedy khi đi cùng * hoặc +)
# {} : Số lần xuất hiện cụ thể. Vd: {2} (2 lần), {2,4} (2 đến 4 lần)
# |  : Hoặc (OR). Vd: "xanh|đỏ"
# () : Gom nhóm (Group) để trích xuất hoặc áp dụng toán tử cho cả nhóm

# --- 3. Special Sequences (Chuỗi đặc biệt) ---
# \d : Chữ số (tương đương [0-9])
# \D : Không phải chữ số
# \w : Ký tự chữ cái, số, gạch dưới [a-zA-Z0-9_]
# \W : Không phải \w
# \s : Khoảng trắng (space, tab, newline)
# \S : Không phải khoảng trắng
# \b : Ranh giới từ (Word boundary). Vd: r"\bain" tìm "ain" trong "rain" nhưng không trong "plain" nếu viết r"\bain"
# \A : Đầu chuỗi (giống ^ nhưng không bị ảnh hưởng bởi multiline flag)
# \Z : Cuối chuỗi (giống $ nhưng không bị ảnh hưởng bởi multiline flag)

# --- 4. Sử dụng Group ---
# Ví dụ: trích xuất phần tên và domain của email
email_pattern = r"([A-Za-z0-9._%+-]+)@([A-Za-z0-9.-]+\.[A-Z|a-z]{2,})"
match_email = re.search(email_pattern, "support@google.com")
if match_email:
    print(f"\n7. Groups:")
    print(f"   - Toàn bộ (group 0): {match_email.group(0)}")
    print(f"   - Tên user (group 1): {match_email.group(1)}")
    print(f"   - Domain   (group 2): {match_email.group(2)}")

# --- 5. re.compile() ---
# Nếu dùng một mẫu regex nhiều lần, nên compile trước để tối ưu hiệu suất.
pattern_digits = re.compile(r"\d+")
result_1 = pattern_digits.findall("abc 123")
result_2 = pattern_digits.findall("xyz 456 789")
print(f"\n8. Compile: {result_1}, {result_2}")

# --- 6. Các Flag phổ biến ---
# re.IGNORECASE (re.I): Không phân biệt hoa thường
# re.MULTILINE (re.M): ^ và $ khớp với đầu/cuối của mỗi dòng (thay vì cả chuỗi)
# re.DOTALL (re.S): Dấu chấm (.) khớp với cả ký tự xuống dòng (\n)
# re.VERBOSE (re.X): Cho phép viết regex trên nhiều dòng và thêm comment

regex_multiline = r"^Dòng"
text_multi = """Dòng 1
Dòng 2
Không phải dòng"""
print(f"\n9. Multiline flag: {re.findall(regex_multiline, text_multi, re.MULTILINE)}")
