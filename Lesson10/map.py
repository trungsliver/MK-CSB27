# ============= MAP ===============

# Tác dụng: biến đổi hàng loạt phần tử của 1 dữ liệu

# Hàm map(function, iterable) 
    # function: là 1 hàm biến đổi phần tử
    # iterable: là 1 đối tượng dữ liệu (list, tuple, set, dict, string)

# Ví dụ: Cho 1 danh sách tên học sinh (viết hoa lộn xộn)
# Yêu cầu: DÙng map biến đổi danh sách tên học sinh thành viết hoa tất cả

students = ['tHe cHUoNg', 'dUc mInH', 'tIeN dUnG', 'mInH NGoC', 'nGOc huY', 'MInH quAn', 'hAI dANg']

# Cách 1: Dùng hàm thông thường
def to_upper(name:str):
    return name.upper()
upper_students_1 = map(to_upper, students)
print('Upper students 1:', list(upper_students_1))

# Cách 2: Dùng hàm không xác định (lambda function)
upper_students_2 = map(lambda name: name.upper(), students)
print('Upper students 2:', list(upper_students_2))