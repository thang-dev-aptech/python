students = [
    ("An", 8, "HN"), ("Bình", 9, "ĐN"),
("Cường", 7, "HCM"),
("Nam", 2, "Huế"),
("Lan", 6, "HN"),
("Huy", 5, "HCM"),
("Trang", 9, "ĐN"),
("Minh", 4, "Huế"),
("Phương", 7, "HN"),
("Tuấn", 3, "HCM")
]


def tong_diem_sinh_vien_hn(list):
    sum = 0
    for ten,diem,tp in list :
        if(tp == 'HN'):
            sum += diem

    return sum

sum = tong_diem_sinh_vien_hn(students)
print(sum) 
        