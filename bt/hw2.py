while True:
    print("\n===== MENU NHÀ HÀNG =====")
    print("1. Chọn món ăn")
    print("2. Danh sách món ăn")
    print("3. Đồ uống free")
    print("4. Thoát")

    choice = input("Nhập lựa chọn của bạn (1-4): ")

    if choice == "1":
        print("Bạn đã chọn: Chọn món ăn")
    elif choice == "2":
        print("Bạn đã chọn: Danh sách món ăn")
    elif choice == "3":
        print("Bạn đã chọn: Đồ uống free")
    elif choice == "4":
        print("Thoát chương trình. Tạm biệt!")
        break
    else:
        print("Chọn sai, vui lòng nhập lại!")