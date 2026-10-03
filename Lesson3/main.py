# Bài 1: Tạo lớp Rectangle với các thuộc tính: length, width.  
# Tạo phương thức tính diện tích và chu vi của hình chữ nhật. 
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def perimeter(self):
        return 2 * (self.length + self.width)
    def area(self):
        return self.length * self.width
    def display_info(self):
        print('===== RECTANGLE =====')
        print('Length:', self.length)
        print('Width:', self.width)
        print('Perimeter:', self.perimeter())
        print('Area:', self.area())
        print('====================')

hcn1 = Rectangle(5, 3)
hcn1.display_info()

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
    def __init__(self, account_number, owner, balance):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def display_balance(self):
        print('\n===== ACCOUNT INFO =====')
        print('Account number:', self.account_number)
        print('Owner:', self.owner)
        print('Balance:', self.balance)

    # Phương thức nạp tiền
    def deposit(self, amount):
        if amount > 0:
            # Cộng tiền vào tài khoản
            self.balance += amount      # self.balance = self.balance + amount
            # Thông báo nạp thành công
            print(f'Nạp thành công ${amount}!')
        else:
            # Thông báo nạp tiền thất bại
            print("Số tiền nạp vào phải lớn hơn 0.")
        # Hiển thị lại thông tin sau khi nạp
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

account1 = BankAccount("123456789", "Tiến Dũng", 1000)
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