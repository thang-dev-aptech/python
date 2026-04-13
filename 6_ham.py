# Hàm (function)

# định nghĩa và gọi hàm 
def greet(name):
    return f"Hello, {name}!"

print(greet("Python"))
# không có tham số
def say_hello():
    return "Hello!"

print(say_hello())  
# hàm chứa tham số 
def add(a, b):
    return a + b
    
print(add(1, 2))

# hàm chứa tham số mặc định 
def add(a, b=0):
    return a + b
    
print(add(1))
print(add(1, 2))

# *args / **kwargs
# *args cho phép truyền tham số không giới hạn (tuple)
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4, 5))
# **kwargs cho phép truyền tham số không giới hạn (dict)
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

print_info(name="Alice", age=25, city="Hanoi")


# phạm vi (scope)
x = 10  # biến global
def test_scope():
    global x   # khai báo để sửa biến global
    x = 20
    y = 5      # biến local
    print("Inside function: x =", x, ", y =", y)

test_scope()
print("Outside function: x =", x)

# decorator
# Decorator là một hàm nhận vào một hàm và trả về một hàm khác

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper
    
@my_decorator
def say_hello():
    print("Hello!")
    
say_hello()

# lambda 

# def square(x): return x * x

square = lambda x: x * x
print(square(5))

def square(x):
    return lambda y: x * y

square_2 = square(2)
print(square_2(5))


# đệ quy (recursion)
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))


# generator (tạo ra iterator)
# generator là các hàm có thể tạm dừng hoặc tiếp tục thực thi 
# example

def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

for num in count_up_to(5):
    print(num)


# Hàm nhận hàm khác làm đối số
def apply_func(func, value):
    return func(value)

print(apply_func(lambda x: x*2, 10))  # 20

