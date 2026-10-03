# Bài 1: Nhập 2 số nguyên a và b từ bàn phím.
# In ra các số nguyên trong khoảng [a, b]
a = int(input('Nhập a: '))
b = int(input('Nhập b: '))
print(f'Các số trong khoảng [{a}, {b}] là:')
for i in range (a, b+1):
    print(i, end = ' ')

# Bài 2: Nhập 1 số nguyên a trong khoảng [1, 10]
# In ra màn hình bảng cửu chương a
a = int(input('\nNhập a: '))
if 1<= a <= 10:
    print(f'Bảng cửu chương {a}:')
    for i in range (1, 11):
        print(f'{a} x {i} = {a*i}')
else:
    print('Số nhập vào không hợp lệ!')

# Bài 3: In ra màn hình bảng cửu chương từ 2 => 9
for a in range(2, 10):
    print(f'\nBảng cửu chương {a}:')
    for i in range (1, 11):
        print(f'{a} x {i} = {a*i}')

# Bài 4: Nhập số nguyên n trong khoảng [0,100]
# nếu nhập sai (n<0 hoặc n>100) thì yêu cầu nhập lại
n = int(input("Nhập số nguyên n (0<=n<=100): "))
while n < 0 or n > 100:
    print("Nhập sai! Vui lòng nhập lại.")
    n = int(input("\nNhập số nguyên n (0<=n<=100): "))
print(f"Nhập n = {n} thành công!" )

# Bài 5: Cho danh sách num_list
num_list = [5, 2, 9, 7, 1, 6, 3, 8, 4]
    # Tính tổng các phần tử chẵn trong danh sách
sum_even = 0
for num in num_list:
    if num % 2 == 0:
        sum_even += num
print(f"Tổng các phần tử chẵn trong danh sách: {sum_even}")

    # Đếm số lượng phần tử lẻ trong danh sách
count_odd = 0
for num in num_list:
    if num % 2 != 0:
        count_odd += 1
print(f"Số lượng phần tử lẻ trong danh sách: {count_odd}")
    # Tìm vị trí phần tử lớn nhất trong danh sách
max_value = max(num_list)
for i in range(len(num_list)):
    if num_list[i] == max_value:
        print(f"Vị trí phần tử lớn nhất trong danh sách: {i}")
        break

# Bài 6: Nhập 1 số nguyên n, Kiểm tra xem n có phải số nguyên tố không?
n = int(input("Nhập số nguyên n: "))
count = 0

for i in range(1, n + 1):
    if n % i == 0:
        count += 1
    if count > 2:
        break

if count == 2:
    print(f"{n} là số nguyên tố")
else:
    print(f"{n} không phải số nguyên tố")

# Bài 7: Viết một hàm sum_odd(numbers) để tính tổng các số lẻ trong một danh sách numbers.
# 	YC1: Hàm nhận vào một danh sách các số nguyên.
# 	YC2: Hàm trả về tổng các số lẻ trong danh sách đó.
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def sum_odd(numbers):
    sum = 0                 # Khai báo biến lưu tổng
    for item in arr:        # Duyệt danh sách, cách 2 - chỉ có giá trị
        if item % 2 != 0:   # Kiểm tra số lẻ
            sum += item     # Cộng giá trị phần tử vào biến sum
    return sum              # Trả về giá trị sum khi duyệt xong vòng lặp

print("Tổng các số lẻ trong danh sách là:", sum_odd(arr))

# Bài 8: Viết một hàm count_words(s) để đếm số lượng từ trong một chuỗi s.
# 	YC1: Hàm nhận vào một chuỗi ký tự s.
# 	YC2: Hàm trả về số lượng từ trong chuỗi đó.

sentence = "Đây là lớp học lập trình tại MindX"

def count_words(s:str):
    # strip(): Loại bỏ khoảng trắng ở đầu và cuối chuỗi
    # split(): Tách chuỗi thành danh sách các từ dựa trên khoảng trắng
    arr = s.strip().split()
    return len(arr)  # Trả về độ dài của danh sách từ

print("Số lượng từ trong chuỗi là:", count_words(sentence)) 