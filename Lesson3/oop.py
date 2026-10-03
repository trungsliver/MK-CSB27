# OOP - Object Oriented Programming
# Lập trình hướng đối tượng

# Tổng quát: là cách mô tả đối tượng ở thế giới thực vào chương trình máy tính

# Class (lớp đối tượng): đối tượng tổng quát
# Object: đối tượng cụ thể

# Ví dụ: Mô tả con người (Human)
    # Thuộc tính (attributes): đặc điểm của đối tượng (name, age, gender)
    # Phương thức (methods): hành động của đối tượng (ăn, ngủ, đi, nói chuyện,..)

# Khai báo lớp đối tượng (class)
class Human:
    # Khởi tạo đối tượng (constructor)
    def __init__(self, name, age, gender):
        # name, age, gender là thuộc tính
        self.name = name
        self.age = age
        self.gender = gender

# Khởi tạo đối tượng cụ thể
human1 = Human('Đức Minh', 2, 'male')
human2 = Human('Thế Chương', 30, 'female')

print(human1)
