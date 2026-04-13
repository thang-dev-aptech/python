# Cấu trúc điều kiện

# if/ elif/ else

age = 18 
if age >= 18:
    print("Đủ 18 tuổi")
elif age < 18:
    print("Chưa đủ 18 tuổi")
else:
    print("Không hợp lệ")

# toán tử 3 ngôi

age = 18
status = "Đủ 18 tuổi" if age >= 18 else "Chưa đủ 18 tuổi"
print(status)

# match/ case

command = "start"

match command:
    case "start":
        print("Hệ thống đang khởi động...")
    case "stop":
        print("Hệ thống đã dừng.")
    case "restart":
        print("Hệ thống khởi động lại.")
    case _:   # default
        print("Lệnh không hợp lệ!")
