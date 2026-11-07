# ================= Ôn tập =================

# Bài 1: Nhập từ bàn phím điểm trung bình của học sinh. Hãy xếp hạng học lực của học sinh đó, biết rằng:
# Giỏi: [8,10], Khá: [6.5, 8), TB: [5, 6.5), Yếu: [0, 5)
# score = float(input("Nhập điểm trung bình của học sinh: "))
score = 7.5

def rank_student(score:float):
    if 8 <= score <= 10:
        print("Học lực: Giỏi")
    elif 6.5 <= score < 8:
        print("Học lực: Khá")   
    elif 5 <= score < 6.5:
        print("Học lực: Trung Bình")
    elif 0 <= score < 5:
        print("Học lực: Yếu")
    else:
        print("Điểm không hợp lệ")

def rank_student2(score:float):
    if score < 0 or score > 10:
        print("Điểm không hợp lệ")
    else:
        if score >= 8:
            print("Học lực: Giỏi")
        elif score >= 6.5:
            print("Học lực: Khá")   
        elif score >= 5:
            print("Học lực: Trung Bình")
        else:
            print("Học lực: Yếu")

rank_student(score)
rank_student2(score)

# Bài 2: Nhập từ bàn phím số giây cần chuyển đổi. In ra màn hình thời gian sau chuyển đổi, định dạng: giờ - phút - giây
# VD: 3661s = 1h 1m 1s
# time = int(input("Nhập số giây cần chuyển đổi: "))
time = 3661

def convert_time(total_seconds:int):
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return f"{total_seconds}s = {hours}h {minutes}m {seconds}s"

print('Kết quả:', convert_time(time))

# Bài 3: Nhập 2 số nguyên a và b từ bàn phím
a = 5
b = 10

# Yêu cầu 1: In ra tất cả các số trong khoảng [a, b] hoặc ngược lại
def print_range(a:int, b:int):
    if a < b:
        for i in range(a, b+1):
            print(i, end=' ')
    else:
        for i in range(a, b-1, -1):
            print(i, end=' ')
print_range(a, b)

# Yêu cầu 2: Tính tổng các số chẵn trong khoảng vừa in
def sum_even(a:int, b:int):
    total = 0
    if a < b:
        for i in range(a, b+1):
            if i % 2 == 0:
                total += i
    else:
        for i in range(b, a+1):
            if i % 2 == 0:
                total += i
    return total
print("\nTổng các số chẵn trong khoảng:", sum_even(a, b))

# Yêu cầu 3: Tính trung bình cộng các số nguyên trong khoảng trên
def average_range(a:int, b:int):
    if a < b:
        count = b - a + 1
        total = sum(range(a, b+1))
    else:
        count = a - b + 1
        total = sum(range(b, a+1))
    return round(total / count, 2)
print("Trung bình cộng các số trong khoảng:", average_range(a, b))

# Bài 4: Viết hàm/chương trình con kiểm tra 1 số có phải là số nguyên tố hay không, biết rằng: số nguyên tố là số chỉ chia hết cho 1 và chính nó.
def is_prime(n:int):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
# In ra số nguyên tố trong khoảng [10,100].
print("Các số nguyên tố trong khoảng [10,100]:")
for num in range(10, 101):
    if is_prime(num):
        print(num, end=' ')

# Bài 5: Nhập vào từ bàn phím 1 chuỗi ký tự bao gồm các số nguyên, các số này cách nhau 1 khoảng trắng (hoặc dấu ,).
input_str = '34 67 23 89 12 45 90 11'

# Yêu cầu 1: Tách chuỗi và thêm vào danh sách có tên num_list
num_list = input_str.split()
print("\nDanh sách num_list:", num_list)

# Yêu cầu 2: Chuyển đổi toàn bộ phần tử trong danh sách num_list thành kiểu dữ liệu int.
for i in range(len(num_list)):
    num_list[i] = int(num_list[i])
print("Danh sách num_list sau khi chuyển đổi:", num_list)

# Yêu cầu 3: In ra màn hình số lượng số lẻ của num_list.
odd_count = 0
for num in num_list:
    if num % 2 != 0:
        odd_count += 1
print("Số lượng số lẻ trong num_list:", odd_count)

# Yêu cầu 4: Sắp xếp các phần tử trong danh sách num_list theo thứ tự từ lớn đến nhỏ.
num_list.sort(reverse=True)
print("Danh sách num_list sau khi sắp xếp từ lớn đến nhỏ:", num_list)

# Bài 6: Dùng thư viên random để thêm ngẫu nhiên các số nguyên trong khoảng [20,50] vào 2 danh sách arr1 và arr2. 
import random
arr1 = [random.randint(20, 50) for _ in range(10)]
arr2 = [random.randint(20, 50) for _ in range(10)]
# Yếu cầu 1: Hãy viết hàm/chương trình con in ra phần tử chung của 2 danh sách vừa tạo.
def print_common_elements(list1, list2):
    common_elements = set(list1) & set(list2)
    return list(common_elements)
print("Phần tử chung của arr1 và arr2:", print_common_elements(arr1, arr2))

def print_common_elements(list1, list2): # Độ phức tạp O(n^2) / O(n*m)
    arr_common = []
    for item in list1:
        if item in list2 and item not in arr_common:
            arr_common.append(item)
    return arr_common
print("Phần tử chung của arr1 và arr2:", print_common_elements(arr1, arr2))

# Yêu cầu 2: In ra màn hình vị trí phần tử nhỏ nhất của danh sách arr1
    # Cách 1:
min_value = min(arr1)
min_index = arr1.index(min_value)
print("Vị trí phần tử nhỏ nhất của arr1:", min_index)
    # cách 2:
min_value2 = arr1[0]
min_index2 = 0
for i in range(1, len(arr1)):
    if arr1[i] < min_value2:
        min_value2 = arr1[i]
        min_index2 = i
print("Vị trí phần tử nhỏ nhất của arr1:", min_index2)

# Yêu cầu 3: In ra màn hình vị trí phần tử lớn nhất của danh sách arr2
max_value = max(arr2)
max_index = arr2.index(max_value)
print("Vị trí phần tử lớn nhất của arr2:", max_index)

# Bài 7: Hãy nhập từ bàn phím họ tên của bạn.
name = 'Bui Duc Trung'
# Yêu cầu 1: Chuyển đổi chuỗi ký tự tên thành chuỗi ký tự viết hoa
print("Tên viết hoa các chữ cái đầu:", name.upper())
# Yêu cầu 2: Chuyển đổi chuỗi ký tự tên thành chuỗi ký tự viết thường
print("Tên viết thường:", name.lower())
# Yêu cầu 1: Chuyển đổi chuỗi ký tự tên thành chuỗi ký tự viết hoa các chữ cái đầu
print("Tên viết hoa các chữ cái đầu:", name.title())
