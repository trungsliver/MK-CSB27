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
    # Duyệt toàn bộ dict
for key, value in dict2.items():
    print(key, ':', value)

# Update - Chỉnh sửa
    # Thêm mới
dict2['hobbies'] = ['Gaming', 'Sleeping']
    # Chỉnh sửa
dict2['name'] = 'Duc Minh Loopy'

# Delete - Xóa dữ liệu
    # Xóa theo key - del
del dict2['school']
    # Xóa theo key và lấy giá trị - pop()
city = dict2.pop('city')
print('City:', city)    

# Kiểm tra key có tồn tại hay không
print('name' in dict2)  # True
print('humor' in dict2)  # False

# Lấy tất cả các key
print('Keys:', dict2.keys())
# Lấy tất cả các value
print('Values:', dict2.values())
# Lây tất cả các cặp key-value
print('Items:', dict2.items())