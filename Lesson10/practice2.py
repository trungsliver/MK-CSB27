# ================  DICTIONARY - MAP ==================

# Bài Tập 1: Quản Lý Thông Tin Sinh Viên
# Yêu cầu: Tạo một dictionary lưu trữ thông tin sinh viên với các khóa: name, age, và grade. 
# Thực hiện các thao tác sau:
# 1. Thêm sinh viên với thông tin name = "John", age = 22, và grade = "A".
student = {
    'name': 'John',
    'age': 22,
    'grade': 'A'
}
# 2. Cập nhật grade của sinh viên thành "A+".
student['grade'] = 'A+'
print('Updated grade:', student['grade'])
# 3. Xóa thông tin age của sinh viên.
del student['age']
print('After deleting age:', student)
# 4. Kiểm tra xem name có trong dictionary không.
print('name' in student)

# Bài Tập 2: Đếm Số Lần Xuất Hiện Của Từ Trong Chuỗi
# Yêu cầu: Viết chương trình nhận vào một chuỗi và trả về một dictionary đếm số lần xuất hiện của mỗi từ trong chuỗi.
sentence = 'this is a test this is only a test'
def word_count(sentence:str):
    # split() để tách chuỗi thành danh sách các từ
    # strip() để loại bỏ khoảng trắng thừa
    words = sentence.lower().strip().split()
    # Mỗi từ sẽ là 1 key, số lần xuất hiện sẽ là value
    count_dict = {}
    for word in words:
        if word in count_dict:
            count_dict[word] += 1
        else:
            count_dict[word] = 1
    return count_dict
print(word_count(sentence))

# Bài Tập 3: Gộp Hai Dictionary
# Yêu cầu: Cho hai dictionary A và B. Viết chương trình gộp chúng lại. Nếu một key xuất hiện ở cả hai dictionary, cộng giá trị của chúng lại.
A = {'a': 100, 'b': 200, 'c': 300}
B = {'b': 250, 'c': 150, 'd': 400}
def merge_dicts(dict1:dict, dict2:dict):
    # tạp bản sao dict1 để đảm bảo dữ liệu không thay đổi
    merged_dict = dict1.copy()
    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value
        else:
            merged_dict[key] = value
    return merged_dict

print('Merged dictionary:', merge_dicts(A, B))

# Bài Tập 4: Tìm Key Có Giá Trị Lớn Nhất
# Yêu cầu: Cho một dictionary có các cặp {key: value}. Viết chương trình để tìm key có giá trị lớn nhất.

# Bài Tập 5: Sắp Xếp Dictionary Theo Giá Trị
# Yêu cầu: Viết chương trình để sắp xếp một dictionary theo giá trị từ cao đến thấp.

# Bài Tập 6: Nhóm Các Phần Tử Theo Giá Trị
# Yêu cầu: Viết chương trình để nhóm các phần tử của một dictionary dựa trên giá trị của chúng. Ví dụ, các phần tử có cùng giá trị sẽ được đưa vào một danh sách.

# Bài Tập 7: Tạo Dictionary Từ Danh Sách
# Yêu cầu: Viết chương trình tạo một dictionary từ hai danh sách: một danh sách chứa key và một danh sách chứa value tương ứng.