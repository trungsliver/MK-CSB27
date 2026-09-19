# Variables - Biến số
    # Dùng để lưu trữ dữ liệu
    # Có thể thay đổi khi lập trình
name = 'Duc Trung'
x,y,z = 1,2,3

# Constant - Hằng số
    # Dùng để lưu trữ dữ liệu
    # Không thể thay đổi khi lập trình
MY_CONSTANT = '132456'

# Quy tắc đặt tên biến:
    # Chỉ gồm ký tự tiếng anh, số, dấu gạch dưới
    # Không được bắt đầu bằng số
    # Không được trùng với từ khóa Python (if, else, for,...)

# 2 kiểu đặt tên phổ biến:
    # camelCase: viết hoa chữ cái đầu mỗi từ, trừ từ đầu tiên
myFullName = 'Bui Duc Trung'
    # snake_case: mỗi từ sẽ cách nhau 1 dấu _
my_full_name = 'Bui Duc Trung'

# Data types - Kiểu dữ liệu
    # String: chuỗi / xâu ký tự
name = 'Duc Trung'
    # int (integer): số nguyên
age = 2
    # float: số thực (có phần thập phân)
score = 8.5
    # bool/boolean: logic (chỉ có 2 giá trị True/False - Đúng/Sai)
is_male = True

# Hàm kiểm tra kiểu dữ liệu: type()
print(type(name))

# Các cách hiển thị dữ liệu
    # Cách 1: Dùng dấu + (nối chuỗi)
print('Họ tên: ' + name)
    # Cách 2: Dùng dấu ,
print('Điểm:', score)
    # Cách 3: Dùng f-string
print(f'Tôi tên là {name}, đang {age} tuổi.')
    # Cách 4: Hiển thị trên nhiều dòng (trích đoạn)
print(f'''
===== THÔNG TIN =====
Họ tên: {name}
Tuổi: {age}
Điểm: {score}
Giới tính nam: {is_male}
=====================''')

    # Lưu ý:
        # \n: xuống dòng
print('Dòng 1 \nDòng 2 \nDòng 3')
        # \t: tab (1 tab = 4 space)
print('Cột 1\tCột 2\tCột 3')

# Nhập dữ liệu - input()
    # Mặc định: dữ liệu nhập vào là string
score1 = input('Nhập điểm: ')
print('Datatype của score1:', type(score1))
    # Xác định kiểu dữ liệu khi nhập
score2 = float(input('Nhập điểm lần 2: '))
print('Datatype của score1:', type(score2))

# Các phép toán:
    # Cơ bản: + - * /
    # Chia lấy nguyên: //
    # Chia lấy dứ: %
    # Lũy thừa: **
# Lưu ý: lũy thừa sẽ thực hiện từ phải qua trái
print('7 / 2 =', 7 / 2)
print('7 // 2 =', 7 // 2)
print('7 % 2 =', 7 % 2)
print('2 ** 2 ** 3 =', 2 ** 2 ** 3)  # 2 ** (2 ** 3) = 2 ** 8 = 256
