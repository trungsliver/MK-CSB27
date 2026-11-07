# ============== ÔN TẬP ==============
# Bài 1: Cho 2 mảng số nguyên nums1 và nums2
# Viết chương trình trả về mảng là giao của 2 mảng trên
# Đánh giá độ phức tạp của thuật toán

    # Khởi tạo 2 danh sách
nums1 = [i for i in range(5,16)]    # 5 đến 15
nums2 = [i for i in range(10,21)]   # 10 dến 20

    # Cách 1: ĐỘ phức tạp O(n^2)
arr1 = []
for item1 in nums1:
    for item2 in nums2:
        if item1 == item2:
            arr1.append(item1)
print("Phép giao tập hợp của 2 mảng là:", arr1)

    # Cách 2: ĐỘ phức tạp O(n log m) 
def binary_search(arr, target):
    arr.sort()      # Sắp xếp mảng để áp dụng tìm kiếm nhị phân
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

arr2 = []
if len(nums1) < len(nums2):
    # swap phần tử 2 danh sách => nums1 luôn là danh sách dài hơn
    nums1, nums2 = nums2, nums1 
for item in nums2:
    if binary_search(nums1, item):
        arr2.append(item)
print("Phép giao tập hợp của 2 mảng là:", arr2)

# Bài 2: Cho mảng nums gồm n quả bóng có màu đỏ, trắng, xanh.
    # Viết chương trình sắp xếp mảng này sao cho:
    # những quả bóng có màu giống nhau thì được sắp xếp cạnh nhau
    # có thứ tự từ đỏ đến trắng đến xanh
    # Đánh giá độ phức tạp của thuật toán.

nums = ['red', 'white', 'blue', 'red', 'white', 'blue', 'red', 'white', 'blue']

def sort_colors(arr): # O(n)
    # Đếm số lượng mỗi màu
    count_red, count_white, count_blue = 0, 0, 0
    for item in arr:
        if item == 'red': count_red += 1
        if item == 'white': count_white += 1
        if item == 'blue': count_blue += 1
    # Tạo mảng mới với thứ tự màu sắc
    sorted_arr = ['red'] * count_red + ['white'] * count_white + ['blue'] * count_blue
    return sorted_arr

print("Mảng sau khi sắp xếp là:", sort_colors(nums))


# ================= LUYỆN TẬP =================
# Thực hiện và xác định độ phức tạp thuật toán của các bài tập sau

# Bài 1: Viết một hàm sum_odd(numbers) để tính tổng các số lẻ trong một danh sách numbers.
# 	YC1: Hàm nhận vào một danh sách các số nguyên.
# 	YC2: Hàm trả về tổng các số lẻ trong danh sách đó.

# Bài 2: Viết một hàm is_prime(n) để kiểm tra xem một số nguyên dương n có phải là số nguyên tố hay không.
# 	YC1: Hàm nhận vào một số nguyên dương n.
# 	YC2: Hàm trả về True nếu n là số nguyên tố, ngược lại trả về False.

# Bài 3: Viết một hàm count_words(s) để đếm số lượng từ trong một chuỗi s.
# 	YC1: Hàm nhận vào một chuỗi ký tự s.
# 	YC2: Hàm trả về số lượng từ trong chuỗi đó.

# Bài 4: Viết một hàm sum_of_digits(n) để tính tổng các chữ số của một số nguyên dương n.
# 	YC1: Hàm nhận vào một số nguyên dương n.
# 	YC2: Hàm trả về tổng các chữ số của n.

# Bài 5: Viết một hàm find_max(numbers) để tìm vị trí số lớn nhất trong một danh sách numbers.
# 	YC1: Hàm nhận vào một danh sách các số nguyên.
# 	YC2: Hàm trả về vị trí số lớn nhất trong danh sách đó.

# Bài 6: Viết một hàm sum_to_n(n) để tính tổng các số từ 1 đến n.
# 	YC1: Hàm nhận vào một số nguyên dương n.
# 	Yc2: Hàm trả về tổng các số từ 1 đến n.