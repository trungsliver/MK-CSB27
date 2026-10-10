# Bài 1: Tạo lớp Rectangle với các thuộc tính: length, width.  
# Tạo phương thức tính diện tích và chu vi của hình chữ nhật. 
class Rectangle:
    # Hàm khởi tạo
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Phương thức tính chu vi
    def perimeter(self):
        return 2 * (self.length + self.width)
    
    # Phương thức tính diện tích
    def area(self):
        return self.length * self.width
    
hcn1 = Rectangle(5, 3)
print(f"Chu vi hình chữ nhật 1: {hcn1.perimeter()}")
print(f"Diện tích hình chữ nhật 1: {hcn1.area()}")

hc2 = Rectangle(10, 4)
print(f"Chu vi hình chữ nhật 2: {hc2.perimeter()}")
print(f"Diện tích hình chữ nhật 2: {hc2.area()}")

# Bài 2: Tạo lớp BankAccount với các thuộc tính: 
            # account_number: số tài khoản 
            # owner: tên chủ tài khoản
            # balance: số dư tài khoản
    # Tạo phương thức:
            # deposit(amount): nạp tiền vào tài khoản
            # withdraw(amount): rút tiền từ tài khoản
            # display_balance(): hiển thị số dư tài khoản
            # (amount: số tiền nạp/rút theo đơn vị $)
class BankAccount:
    # Hàm khởi tạo
    def __init__(self, account_number, owner, balance):
        # Số tài khoản
        self.account_number = account_number
        # Tên chủ tài khoản
        self.owner = owner
        # Số dư tài khoản
        self.balance = balance

    # Phương thức hiển thị số dư tài khoản
    def display_balance(self):
        print(f'''
========== SỐ DƯ TÀI KHOẢN ==========
Số tài khoản: {self.account_number}
Chủ tài khoản: {self.owner}
Số dư: ${self.balance}
=====================================
''')
        
    # Phương thức nạp tiền
    def deposit(self, amount):
        # amount: số tiền nạp vào tài khoản
        if amount > 0:
            # Cộng tiền vào số dư tài khoản
            self.balance += amount
            # Thông báo nạp tiền thành công
            print(f"Nạp thành công ${amount}!")
        else:
            # Thông báo nạp tiền thất bại
            print("Số tiền nạp vào phải lớn hơn 0.")
        # Hiển thị số dư tài khoản sau khi nạp tiền
        self.display_balance()  

    # Phương thức rút tiền
    def withdraw(self, amount):
        # amount: số tiền rút từ tài khoản
        if amount > 0 and amount <= self.balance:
            # Trừ tiền từ số dư tài khoản
            self.balance -= amount
            # Thông báo rút tiền thành công
            print(f"Rút thành công ${amount}!")
        else:
            # Thông báo rút tiền thất bại
            print("Số tiền rút không hợp lệ!")
        # Hiển thị số dư tài khoản sau khi rút tiền
        self.display_balance()

account1 = BankAccount("123456789", "Hải Nam", 1000)
account1.display_balance()
account1.deposit(500)           # Số dư: $1500
account1.deposit(-200)          # Số dư: $1500 (nạp thất bại)
account1.withdraw(1200)         # Số dư: $300
account1.withdraw(500)          # Số dư: $300 (rút thất bại)

# Bài 3:
    # Tạo class Animal gồm các thuộc tính: tên, loài
    # Viết 2 phương thức cho class Animal

    # Tạo class Dog kế thừa từ class Animal và có thêm thuộc tính: giống
    # Viết 1 phương thức kế thừa từ class Animal (có sửa đổi)
    # Viết 1 phương thức mới cho class Dog
class Animal:
    def __init__(self, name, species):
        self.name = name            # Tên động vật
        self.species = species      # Loài động vật

    def display_info(self):
        print(f'''
======== THÔNG TIN =======
Tên:    {self.name}
Loài:   {self.species}
==========================''')

    def eat(self, food):
        print(f"{self.name} đang ăn {food}.")

class Dog(Animal):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed      # giống / chủng loại
    
    # Tính đa hình
    def display_info(self):
                print(f'''
======== THÔNG TIN =======
Tên:    {self.name}
Loài:   {self.species}
Giống:  {self.breed}
==========================''')
                
    # để sử dụng được print()
    def __str__(self):
        return f"Dog(Name: {self.name}, Species: {self.species}, Breed: {self.breed})"
    
# Bài 4:
    # Hãy xây dựng các lớp cha và lớp con như đã xác định. Lưu ý lớp cha có những đặc điểm sau:
    # 	hang: Tên của hãng xe
    # 	mau_sac: Màu sắc của xe
    # 	gia_tien: GIá tiền của xe.
    # Phương thức khoi_dong(): In ra màn hình “Xe {hãng} đang khởi động”

    # Lớp con có những phương thức sau khác lớp cha:
    # 	Phương thức dap_bang_hai_chan(): In ra màn hình “Xe {hãng} đang được đạp về phía trước”
    # 	Phương thức chay_bang_bon_banh(): In ra màn hình “Xe {hãng} đang chạy về phía trước bằng động cơ”
    # Hãy chọn phương thức phù hợp với từng lớp và hoàn thiện các lớp con có sử dụng kế thừa.
class Vehicle:
    def __init__(self, brand, color, price):
        self.brand = brand
        self.color = color
        self.price = price

    def start(self):
        print(f"Xe {self.brand} đang khởi động")

class Bicycle(Vehicle):
    def __init__(self, brand, color, price):
        super().__init__(brand, color, price)

    def start(self):
        print(f"Xe đạp {self.brand} đang được đạp về phía trước")

class Car(Vehicle):
    def __init__(self, brand, color, price):
        super().__init__(brand, color, price)

    def start(self):
        print(f"Xe ô tô {self.brand} đang chạy về phía trước bằng động cơ")