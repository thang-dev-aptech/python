# arrays mảng trong python 
# các hàm build-in sử dụng với mảng 

from time import process_time
fruit = ["apple", "banana", "cherry"]

# len() trả ra chiều dài của mảng 
print(len(fruit))

# max() trả ra giá trị lớn nhất trong mảng 
print(max(fruit))

# min() trả ra giá trị nhỏ nhất trong mảng 
print(min(fruit))

# sum() trả ra tổng của mảng (chỉ dùng cho số)
# print(sum(fruit)) # Lỗi vì không cộng được chuỗi

# sort() sắp xếp mảng 
fruit.sort()
print(fruit)

# các tham số ở sorted 
print(sorted)

# reverse() đảo ngược mảng 
fruit.reverse()
print(fruit)

# append() thêm phần tử vào mảng 
fruit.append("orange")
print(fruit)

# remove() xóa phần tử trong mảng 
fruit.remove("banana")
print(fruit)

# pop() xóa phần tử trong mảng 
fruit.pop()
print(fruit)

# index() trả ra vị trí của phần tử trong mảng 
print(fruit.index("apple"))

# count() trả ra số lần xuất hiện của phần tử trong mảng 
print(fruit.count("apple"))

# copy() sao chép mảng 
copy_fruit = fruit.copy()
print(copy_fruit)

# clear() xóa toàn bộ mảng 
fruit.clear()
print(fruit)

# del xóa mảng 
del fruit
# print(fruit) # Lỗi: NameError vì biến fruit đã bị xóa khỏi bộ nhớ
    