# range() là hàm build-in trong python 
# range() có 3 tham số : start, stop, step
# range(start, stop, step)

x = range(10) # khi có 1 tham số thì stop nhé nhận (0->9)

y = range(1, 10) # khi có 2 tham số thì start và stop nhé nhận (1->9)

z = range(1, 10, 2) # khi có 3 tham số thì start, stop và step nhé nhận (1->9, 2)

# scope của range
#  thường được sử dụng trong vòng lặp for 
for i in range(5):
    print(i)

# slising 
r = range(1, 10, 2)
print(r[0]) # trả ra giá trị đầu tiên
print(r[:1]) # trả ra một đối tượng range

# kiểm tra xem một số có trong range hay không
print(5 in r)
print(5 not in r)

# chiều dài 
print(len(r))

