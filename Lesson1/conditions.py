# Toán tử quan hệ (so sánh)
    #  So sánh bằng: ==
print('5 == 5', 5 == 5)         # True
print('6 == 5', 6 == 5)         # False
    #  So sánh khác: !=
print('5 != 5', 5 != 5)         # False
print('6 != 5', 6 != 5)         # True
    #  So sánh lớn / nhỏ hơn: > <
print('5 > 5', 5 > 5)           # False
print('4 < 5', 4 < 5)           # True
    # So sánh lớn / nhỏ hơn hoặc bằng: >= <=
print('5 >= 5', 5 >= 5)         # True
print('4 <= 5', 4 <= 5)         # True

# Toán tử logic: and (&&), or (||), not (!)
# Ví dụ: trà sữa - gàn rán

# Câu điều kiện (3 dạng)
    # Dạng thiếu 
age = 2
if age >= 18:
    print('Bạn đã đủ tuổi lái xe')

    # Dạng đủ
num = 2
if num % 2 == 0:
    print(num, 'là số chẵn')
else:
    print(num, 'là số lẻ')

    # Dạng đa nhánh
score = 8.5
if 8 <= score <= 10:
    print('Học lực: Giỏi')
elif 6.5 <= score < 8:
    print('Học lực: Khá')
elif 5 <= score < 6.5:
    print('Học lực: Trung bình')
elif 0 <= score < 5:
    print('Học lực: Yếu')
else:
    print('Điểm không hợp lệ')

# Switch-case statement
day = 3
match day:
    case 1:
        print('Sunday')
    case 2:
        print('Monday')
    case 3:
        print('Tuesday')
    case 4:
        print('Wednesday')
    case 5:
        print('Thursday')
    case 6:
        print('Friday')
    case 7:
        print('Saturday')
    case _: # default case
        print('Day is not valid')

# Kiểm tra lỗi
    # Máy tính sẽ thử chạy câu lệnh trong "try"
    # Nếu đúng: chạy bình thường, bỏ qua câu lệnh trong except
    # Nếu sai: bỏ qua câu lệnh trong try, chạy câu lệnh trong except
try:
    num = 'hihi'
    print("num // 2 =", num // 2)
except:
    print("Lỗi xảy ra khi thực hiện")