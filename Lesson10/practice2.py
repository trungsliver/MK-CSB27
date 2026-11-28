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
# Ví dụ: Với chuỗi "hello world hello", kết quả sẽ là {'hello': 2, 'world': 1}.
sentence = 'this is a test this is only a test'
def word_count(sentence:str):
    # strip() để loại bỏ khoảng trắng thừa ở đầu và cuối
    # split() để tách chuỗi thành các từ dựa trên khoảng trắng
    words = sentence.strip().split()
    # mỗi từ sẽ là key, giá trị là số lần xuất hiện
    count_dict = {}
    for word in words:
        if word in count_dict:
            count_dict[word] += 1
        else:
            count_dict[word] = 1
    return count_dict
print('Word count:', word_count(sentence))

# Bài Tập 3: Gộp Hai Dictionary
# Yêu cầu: Cho hai dictionary A và B. Viết chương trình gộp chúng lại. Nếu một key xuất hiện ở cả hai dictionary, cộng giá trị của chúng lại.
A = {'a': 100, 'b': 200, 'c': 300}
B = {'b': 250, 'c': 150, 'd': 400}
def merge_dicts(dict1:dict, dict2:dict):
    # Copy dict1 để đảm bảo dữ liệu không bị thay đổi
    merged = dict1.copy()
    for key, value in dict2.items():
        if key in merged:
            merged[key] += value
        else:
            merged[key] = value
    return merged
merged_dict = merge_dicts(A, B)
print('Merged dictionary:', merged_dict)

# Bài Tập 4: Tìm Key Có Giá Trị Lớn Nhất
# Yêu cầu: Cho một dictionary có các cặp {key: value}. Viết chương trình để tìm key có giá trị lớn nhất.
scores = {
    'MA': 9,
    'TH': 8.5,
    'LK': 1,
    'DA': 8,
    'TL': 7.5
}
def find_max_key(dict:dict):
    max_key = max(dict, key=dict.get)
    return max_key
max_key = find_max_key(scores)
print('Key with the highest value:', max_key)

# Bài Tập 5: Sắp Xếp Dictionary Theo Giá Trị
# Yêu cầu: Viết chương trình để sắp xếp một dictionary theo giá trị từ cao đến thấp.
scores = {
    'MA': 9,
    'TH': 8.5,
    'LK': 1,
    'DA': 8,
    'TL': 7.5
}
def sort_dict_by_value(dict:dict):
    sorted_items = sorted(dict.items(), key=lambda item: item[1], reverse=True)
    return sorted_items
sorted_scores = sort_dict_by_value(scores)
print('Dictionary sorted by value:', sorted_scores)

# Bài Tập 6: Nhóm Các Phần Tử Theo Giá Trị
# Yêu cầu: Viết chương trình để nhóm các phần tử của một dictionary dựa trên giá trị của chúng. Ví dụ, các phần tử có cùng giá trị sẽ được đưa vào một danh sách.
data = {
    'apple': 1,
    'banana': 2,
    'cherry': 2,
    'date': 3,
    'elderberry': 3
}
def group_by_value(dict:dict):
    group = {}
    for key, value in dict.items():
        if value not in group:
            group[value] = []
        group[value].append(key)
    return group
grouped_data = group_by_value(data)
print('Grouped by value:', grouped_data)

# Bài Tập 7: Tạo Dictionary Từ Danh Sách
# Yêu cầu: Viết chương trình tạo một dictionary từ hai danh sách: một danh sách chứa key và một danh sách chứa value tương ứng.
keys = ['apple', 'banana', 'cherry']
values = [1, 2, 3]
def list_to_dict(keys, values):
    # zip(): tạo ra các cặp key-value từ 2 danh sách
    # dict(): chuyển các cặp key-value thành dictionary
    return dict(zip(keys, values))
print(list_to_dict(keys, values))