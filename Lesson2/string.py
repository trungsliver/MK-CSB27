# String: chuỗi / xâu ký tự
name = 'Ngoc Huy'

# len(): độ dài / số lượng ký tự của chuỗi
print('Số ký tự của name:', len(name))

# Truy cập ký tự bầng index
print('Vị trí chữ u:', name[6])
print('Vị trí chữ c:', name[3])

# Duyệt string
    # Cách 1: Dùng cả index và value
for i in range(len(name)):
    print(f'Index: {i}, Value: {name[i]}')
    # Cách 2: chỉ dùng value
for char in name:
    print(char)

# Xâu con (sub string)
str1 = 'Duc Minh thich mau hong'
str2 = 'Duc Minh'
str3 = 'dep trai'
    # kiểm tra sub string: in
print('str2 in str1:', str2 in str1)
print('str3 in str1:', str3 in str1)
    # Tìm vị trí sub string: 
print('Vị trí từ "Minh":', str1.find('Minh')) # 4
print('Vị trí từ "gf":', str1.find('gf')) # -1: không tìm thấy

# Slicing: cắt chuỗi
name = 'hahahihihuhu'
    # cắt ở vị trí bắt kì [start:stop]
print("name[4:8]:", name[4:8])
    # cắt từ đầu đến vị trị trí bất kì [:stop]
print('name[:4]:', name[:4])
    # cắt từ vị trí bất kì đến hết [start:]
print('name[8:] =', name[8:]) 

# Tách string => trả về danh sách: split()
    # Mặc định tách khi gặp khoảng trắng
str1 = '1 2 3 4 5'
arr1 = str1.split()
print(arr1)
    # Tách khi gặp ký tự bất kì
str2 = 'a,b,c,d,e,f,g'
arr2 = str2.split(',')
print(arr2)

# Xóa khoảng trắng ở đầu và cuối chuỗi: strip()
name = '     Minh Ngọc        '
print('Trước strip:', name)
name2 = name.strip()
print('Sau strip:', name2)

# Thay thế substring: replace()
song = 'baby shark doo doo doo doo doo doo'
    # Thay thế toàn bộ: replace(old, new)
song2 = song.replace('doo', 'minh')
print(song2)
    # Thay thế 1 phần: replace(old, new, count)
song3 = song.replace('doo', 'minh', 3)
print(song3)

# Kết hợp chuỗi : join()
arr = ['r','o','n','a','l','d','o']
    # Kết hợp với khoảng trắng
str1 = ' '.join(arr)
print(str1)
    # Kết hợp với ký tự bất kì
str3 = '-'.join(arr)
print(str3)

# Chuẩn hóa string
name = 'nGuYeN vAn HaI dANg'
    # Viết hoa tất cả: upper()
print(name.upper())
    # Viết thường tất cả: lower()
print(name.lower())
    # Viết hoa chữ cái đầu: title()
print(name.title())

# Bài tập 1: Chuyển đổi kiểu dữ liệu danh sách: str => int
arr = ['1', '2', '3', '4', '5', '6', '7', '8', '9']  # string
    # Cách 1:
arr1 = []
for item in arr:
    new_item = int(item)
    arr1.append(new_item)
print('arr1 =', arr1)      # int
    # Cách 2:
arr2 = [int(item) for item in arr]
print('arr2 =', arr2)      # int
