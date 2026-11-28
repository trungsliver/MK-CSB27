# Bài 1: Tạo Stack và thực hiện push/pop
# Yêu cầu:
# 	- Tạo Stack
# 	- Thêm các số: 1, 2, 3
# 	- Lấy ra 1 phần tử
# 	- In Stack

# Bài 2: Đảo ngược chuỗi bằng Stack
# Yêu cầu:
# 	- Nhập chuỗi "python"
# 	- Dùng Stack để đảo ngược

# Bài 3: Kiểm tra dấu ngoặc hợp lệ
# Chuỗi được gọi là hợp lệ nếu:
#     	1. Các dấu ngoặc mở và ngoặc đóng khớp với nhau đúng thứ tự: () [] {}
#     	2. Mỗi dấu ngoặc mở phải có dấu ngoặc đóng tương ứng
# Gợi ý:
#     	- Dùng stack để lưu các dấu ngoặc mở.
#     	- Khi gặp dấu ngoặc đóng, kiểm tra xem nó có khớp với dấu ngoặc mở trên cùng của stack không.

# Bài 4: Đóng vai trò là 1 lập trình viên xây dựng ứng dụng web đơn giản. Hãy phát triển 2 chức năng:
# 	- Back: quay lại trang web trước đó
# 	- Forward: tiến tới trang web bạn vừa quay lại
# Yêu cầu: xây dựng lớp Browser có 3 phương thức (visit_page, back, forward)
# Gợi ý: sử dụng 2 stack để lưu lịch sử back và lịch sử forward