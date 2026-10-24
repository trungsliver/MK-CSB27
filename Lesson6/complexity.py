# COMPLEXITY - Độ phức tạp của thuật toán

# Khái niệm thuật toán: tập hợp các bước để giải quyết 1 vấn đề

# Độ phức tạp của thuật toán:
    # Dùng để đo lường hiệu quả của thuật toán
    # Biểu diễn bằng Big-O Notation
        # Độ phức tạp: (O) = n * số phép toán (số bước)
        # n là kích thước của dữ liệu đầu vào

# Ví dụ về độ phức tạp của thuật toán:

# O(1) - độ phức tạp hằng số (constant): gán, nhập, xuất, tính toán cơ bản
name = 'Duc Trung'
print(name)
print(1+1)

# O(n) - tuyến tính
a = [1, 2, 3, 4, 5]     # n = 5
for item in a:
    print(item)         

# O(n^2) - bậc hai, vòng lặp lồng nhau
    # In ra màn hình bảng cửu chương từ 1 đến 10
for i in range(1, 11):          # n = 10
    print(f'\nBảng cửu chương {i}:')
    for j in range(1, 11):      # n = 10
        print(f'{i} x {j} = {i*j}')

# O(log n) - logarit
    # Ví dụ: 2^3 = 8, log2(8) = 3
    # Game đoán số: chọn 1 số ngẫu nhiên trong khoảng [1, 100] => chọn số 67
        # đoán tuần tự (tuyến tính) => 67 lần đoán, trường hợp tệ nhất là 100 lần
        # logarit: 50 -> 75 -> 62 -> 68 -> 65 -> 66 -> 67
        # Trường hợp xấu nhất log2(100) = 6.64 ~ 7 lần đoán

# So sánh thời gian thực hiện: O(n^2) > O(n) > O(log n) > O(1)