# Function: hàm / chương trình con
# Ý nghĩa: gom tập hợp các câu lệnh có thể tái sử dụng

    # Hàm không có giá trị trả về
def say_hello():
    print('Hello Trung')
    print('Hello Dũng')
say_hello()
say_hello()

    # Tham số truyền vào
def say_hello2(name):
    print("hello", name)
say_hello2('Ngọc Huy')

    # Giá trị trả về
def add(a:float, b:float) -> float:
    return a + b
add(9, 4)
print(add(5, 6.5))