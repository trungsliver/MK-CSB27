# Đề bài: Tạo Mysterious Game
    # Yêu cầu: tạo ra 1 số đặc biệt để đoán (random)
    # Người chơi cần nhập đến khi nào đoán đúng số đặc biệt thì dừng game

import random
# Tạo 1 số ngẫu nhiên trong khoảng [1, 100]
number = random.randint(1, 100)

# In ra số đặc biệt để kiểm tra
print("Số đặc biệt:", number)  

# Số lần đoán 
count = 1
guess = int(input("Hãy đoán số đặc biệt (1-100): "))

while guess != number:
    if guess < number:
        print("Số bạn đoán nhỏ hơn số đặc biệt.")
    else:
        print("Số bạn đoán lớn hơn số đặc biệt.")
    guess = int(input("\nHãy đoán lại số đặc biệt (1-100): "))
    count += 1

print(f"Bạn đã đoán đúng số đặc biệt {number} sau {count} lần đoán.")