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

    # Phương thức hiển thị
    def __str__ (self):
        return f'{self.name} - {self.age} - {self.gender}'

    # Phương thức hiển thị thông tin
    def display_info(self):
        print('===== HUMAN INFO =====')
        print('Name:', self.name)
        print('Age:', self.age)
        print('Gender:', self.gender)
        print('=====================')

    # phương thức hát
    def sing(self, song):
        print(f'{self.name} is singing {song}')

# Khởi tạo đối tượng cụ thể
human1 = Human('Đức Minh', 2, 'male')
human2 = Human('Thế Chương', 30, 'female')
    # Test phương thức
print(human1)
human2.display_info()
human1.sing('Baby Shark')

# 4 tính chất của lập trình hướng đối tượng:
    # Đóng gói (Encapsulation): che dữ liệu (password, info,...)
    # Kế thừa (Inheritance): dùng lại dữ liệu cũ
    # Đa hình (Polymorphism): cùng 1 tên hàm, hành động khác nhau
    # Trừu tượng (Abstraction): khai báo phương thức trước, ghi hành động sau

# Tính chất kế thừa
class Student(Human):
    def __init__(self, name, age, gender, school):
        # Gọi lại phương thức khởi tạo của lớp cha (Human)
        super().__init__(name, age, gender)
        self.school = school

    # Tính đa hình
    def display_info(self):
        print('===== HUMAN INFO =====')
        print('Name:', self.name)
        print('Age:', self.age)
        print('Gender:', self.gender)
        print('School:', self.school)
        print('=====================')

# Khởi tạo đối tượng student
stu1 = Student('Hải Đăng', 14, 'male', 'Tây Thạnh')
stu1.display_info()