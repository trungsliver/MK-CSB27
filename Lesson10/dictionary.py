# =============== DICTIONARY ======================

# Đặc điểm:
    # Là 1 cấu trúc dữ liệu
    # Đặc trưng: key - value 

# Create - Khởi tạo
    # Tạo dict rỗng
dict1 = {}
    # Tạo dict có dữ liệu
dict2 = {
    # key: value
    'name': ' Duc Minh',
    'age': 14,
    'city': 'Ha Noi',
    'school': 'Vinschool Times City'
}

# Read - Đọc dữ liệu
    # Truy cập bằng key
print('Name:', dict2['name'])
    # Truy cập bằng get()
print('Age:', dict2.get('age'))
        # key không tồn tại -> None
print('Cash:', dict2.get('cash'))
        # key không tồn tại -> giá trị mặc định
print('Girlfriend:', dict2.get('girlfriend', '404 not found'))