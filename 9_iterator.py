"""
KIẾN THỨC VỀ ITERATOR TRONG PYTHON
----------------------------------

1. Khái niệm:
   - Iterable: Là một đối tượng có thể lặp qua các phần tử của nó (ví dụ: list, tuple, dictionary, set, string).
     Iterable có phương thức `__iter__()` trả về một Iterator.
   - Iterator: Là một đối tượng đại diện cho một luồng dữ liệu. Nó trả về dữ liệu từng phần tử một.
     Iterator phải có 2 phương thức:
     1. `__iter__()`: Trả về chính nó.
     2. `__next__()`: Trả về phần tử tiếp theo. Nếu hết phần tử thì raise lỗi StopIteration.

2. Cách hoạt động:
   Khi dùng vòng lặp `for`, Python tự động gọi `iter()` để lấy iterator, sau đó gọi `next()` liên tục cho đến khi gặp StopIteration.
"""

print("--- 1. Ví dụ về Iterable và Iterator ---")
my_list = [1, 2, 3]  # Đây là một Iterable
print(f"my_list là Iterable: {my_list}")

# Lấy Iterator từ Iterable
my_iterator = iter(my_list)
print(f"Iterator lấy từ list: {my_iterator}")

# Dùng next() để lấy từng phần tử
print(next(my_iterator))  # 1
print(next(my_iterator))  # 2
print(next(my_iterator))  # 3

# Nếu gọi tiếp next() sẽ bị lỗi StopIteration vì hết phần tử
# print(next(my_iterator)) # Uncomment dòng này để thấy lỗi

print("\n--- 2. Vòng lặp For hoạt động như thế nào ---")
# Đây là cách vòng for hoạt động "ngầm"
print("Mô phỏng vòng lặp for:")
it = iter(my_list)
while True:
    try:
        val = next(it)
        print(val)
    except StopIteration:
        break

print("\n--- 3. Tự tạo Iterator (Custom Iterator) ---")
class PowTwo:
    """Class triển khai iterator trả về lũy thừa của 2: 2^0, 2^1, ..."""
    def __init__(self, max_pow=0):
        self.max_pow = max_pow
        self.n = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.n <= self.max_pow:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration

# Sử dụng Custom Iterator
pow2 = PowTwo(4)  # 2^0 đến 2^4
print("Các lũy thừa của 2 từ 0 đến 4:")
for i in pow2:
    print(i)

print("\n--- 4. Generators (Cách đơn giản để tạo Iterator) ---")
# Generator là một hàm trả về một iterator, dùng từ khóa `yield`
def my_generator(n):
    value = 0
    while value < n:
        yield value
        value += 1

print("Dùng Generator:")
gen = my_generator(3)
for i in gen:
    print(i)

print("\n--- 5. Iterator vô hạn (Infinite Iterator) ---")
# Cẩn thận khi dùng iterator vô hạn, phải có điều kiện dừng
class InfiniteNumbers:
    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        num = self.num
        self.num += 1
        return num

inf_iter = iter(InfiniteNumbers())
print("3 số đầu tiên từ Iterator vô hạn:")
print(next(inf_iter))
print(next(inf_iter))
print(next(inf_iter))
