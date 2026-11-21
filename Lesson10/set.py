# ================== SET ==================

# Đặc điểm:
    # Là 1 cấu trúc dữ liệu
    # Đặc trưng: không có thứ tự, không chứa các phần tử trùng lặp

# Create - Khởi tạo
    # Tạo set rỗng
set1 = set()
    # Tạo set có dữ liệu
set2 = {1, 2, 3, 4, 5}

# Các thao tác cơ bản
    # Thêm phần tử - add()
set2.add(6)
    # Xóa phần tử 
        # remove(): nếu không có phần tử -> báo lỗi
set2.remove(6)
        # discard(): nếu không có phần tử -> không báo lỗi
set2.discard(7)
print('Set 2:', set2)
    # Duyệt phần tử trong set
for item in set2:
    print(item)

# Các thao tác khác
set3 = {1, 2, 3, 4, 5}
set4 = {4, 5, 6, 7, 8}

    # intersection (phép giao): lấy các phần tử chung
print('Intersection:', set3.intersection(set4))
print('Intersection (operator):', set3 & set4)

    # union (phép hợp): lấy tất cả các phần tử
print('Union:', set3.union(set4))
print('Union (operator):', set3 | set4)

    # difference (phép hiệu): lấy các phần tử của set1 mà không có trong set2   
print('Difference:', set3.difference(set4))
print('Difference (operator):', set3 - set4)