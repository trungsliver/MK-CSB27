# Thao tác: CRUD (Create, Read, Update, Delete)

# Create - Khởi tạo
    # Tạo danh sách rỗng
arr = []
    # Tạo danh sách có sẵn phần tử
csb27 = ['Dũng', 'Minh', 'Ngọc', 'Đăng', 'Huy', 'Chương']
arr1 = ['Đức Minh', 14, 1.7, True, [7, 8.5, 9, 6.5, 9.5]]

# Read - Duyệt / hiện phần tử
    # len(): độ dài/ số lượng phần tử
print('Số lượng phần tử của arr:', len(arr))
print('Số lượng phần tử của arr1:', len(arr1))
    # Hiển thị phần tử bằng index
print('Phần tử đầu tiền:', csb27[0])
print('Phần tử index=3:', csb27[3])
print('Phần tử cuối cùng:', csb27[len(csb27)-1])
print('Phần tử cuối cùng:', csb27[-1])
    # Duyệt và hiện phần tử
        # Cách 1: Dùng cả index và value
for i in range(len(csb27)):
    print(f'Index: {i}, Value: {csb27[i]}')
        # Cách 2: Dùng value
for item in csb27:
    print('Value:', item)
        # Cách 3: Dùng hàm có sẵn enumerate()
for index, value in enumerate(csb27):
    print(f'Index: {index}, Value: {value}')
    # Hiện toàn bộ phần tử (để test)
print(csb27)

# Update - Cập nhật phần tử
    # Thêm vào cuối danh sách - append(value)
csb27.append('Trung')
    # Thêm vào vị trí chỉ định - insert(index, value)
csb27.insert(2, 'Donald Trump')
    # Cập nhật phần tử
csb27[2] = 'Putin'

# Delete - Xóa phần tử
    # Xóa bằng value - remove(value)
csb27.remove('Trung')
    # Xóa bầng index - pop(index)
csb27.pop(2)
    # Xóa tất cả phần tử - clear()
csb27.clear()

# Sắp xếp
num_list = [5, 2, 9, 7, 1, 6, 3, 8, 4]
    # Sắp xếp tăng dần - sort()
num_list.sort()
print(num_list)
    # Sắp xếp giảm dần - sort(reverse=True)
num_list.sort(reverse=True)
print(num_list)

# Tìm phần tử có giá trị lớn nhất / nhỏ nhất
print('Max value:', max(num_list))
print('Min value:', min(num_list))

# Tìm vị trí phần tử lớn nhất / nhỏ nhất
print('Index of max value:', num_list.index(max(num_list)))
print('Index of min value:', num_list.index(min(num_list)))

