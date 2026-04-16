# ================================
# 1. INDENTATION TRONG PYTHON
# ================================
# Indentation (thụt lề) dùng để xác định khối lệnh trong Python.
# Không dùng {} như Java/C.

if 5 > 3:
    print("Đúng")
    print("Vẫn trong if")

print("Ngoài if")


# ================================
# 2. HÀM TRONG PYTHON
# ================================
# Hàm là khối code để tái sử dụng

def tinh_tong(a, b):
    return a + b

print("Tổng:", tinh_tong(3, 4))


# ================================
# 3. LAMBDA
# ================================
# Lambda là hàm ẩn danh, viết ngắn gọn

tinh_tong_lambda = lambda a, b: a + b
print("Lambda:", tinh_tong_lambda(2, 3))


# ================================
# 4. KIỂU DỮ LIỆU
# ================================
# List: có thứ tự, thay đổi được, cho phép trùng
a = [1, 2, 2]

# Tuple: có thứ tự, không thay đổi
b = (1, 2, 3)

# Set: không trùng, không có thứ tự
c = {1, 2, 2}

# Dictionary: key-value
d = {"ten": "An", "tuoi": 20}

print("List:", a)
print("Tuple:", b)
print("Set:", c)
print("Dict:", d)


# ================================
# 5. BÀI TẬP HỌC SINH
# ================================

import random

mon_hoc_list = ["Toán", "Lý", "Hóa", "Văn", "Anh", "Sử", "Địa"]

danh_sach_hs = []

# Tạo 10 học sinh
for i in range(10):
    hs = {
        "ten": f"HS{i+1}",
        "tuoi": random.randint(18, 25),
        "mon_hoc": set(random.sample(mon_hoc_list, 3))
    }
    danh_sach_hs.append(hs)

print("\nDanh sách học sinh:")
for hs in danh_sach_hs:
    print(hs)


# 1. Tìm tất cả môn học
tat_ca_mon = set()

for hs in danh_sach_hs:
    tat_ca_mon.update(hs["mon_hoc"])

print("\nTất cả môn học:", tat_ca_mon)


# 2. Tính tuổi trung bình
tong_tuoi = sum(hs["tuoi"] for hs in danh_sach_hs)
tuoi_tb = tong_tuoi / len(danh_sach_hs)

print("Tuổi trung bình:", tuoi_tb)


# 3. Sinh viên > 21 tuổi và học Địa
print("\nSinh viên >21 tuổi và học Địa:")
for hs in danh_sach_hs:
    if hs["tuoi"] > 21 and "Địa" in hs["mon_hoc"]:
        print(hs)
