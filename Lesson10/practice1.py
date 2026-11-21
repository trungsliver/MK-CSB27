# =============== LUYỆN TẬP SET ===============
# Bài Tập 1: Tạo Tập Hợp Và Thực Hiện Các Thao Tác
# Yêu cầu: Tạo hai tập hợp A = {1, 2, 3, 4, 5} và B = {4, 5, 6, 7, 8}. Thực hiện các thao tác sau:
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
# 	1. Thêm phần tử 9 vào tập hợp A.
A.add(9)
print("Set A after adding 9:", A)
# 	2. Xóa phần tử 4 khỏi tập hợp B.
B.remove(4)
print("Set B after removing 4:", B)
# 	3. Tìm hợp, giao, hiệu của hai tập hợp A và B.
set_union_AB = A.union(B)
set_intersection_AB = A.intersection(B)
set_difference_AB = A.difference(B)

print("Union of A and B:", set_union_AB)
print("Intersection of A and B:", set_intersection_AB)
print("Difference of A and B (A - B):", set_difference_AB)

# Bài Tập 2: Kiểm Tra Tập Hợp
# Yêu cầu: Cho tập hợp C = {'apple', 'banana', 'cherry'}. 
# Kiểm tra xem 'banana' và 'grape' có trong tập hợp không.
C = {'apple', 'banana', 'cherry'}
print("'banana' in C:", 'banana' in C)  # True
print("'grape' in C:", 'grape' in C)    # False