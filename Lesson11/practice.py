# Bài 1: Tạo Stack và thực hiện push/pop
# Yêu cầu:
# 	- Tạo Stack
stack = []
# 	- Thêm các số: 1, 2, 3
stack.append(1)
stack.append(2)
stack.append(3)
# 	- Lấy ra 1 phần tử
top_element = stack.pop()
print('Phần tử vừa xóa:', top_element)
# 	- In Stack
print('Sau khi xóa:', stack)

# Bài 2: Đảo ngược chuỗi bằng Stack
# Yêu cầu:
# 	- Nhập chuỗi "python"
# 	- Dùng Stack để đảo ngược
input_string = "python"
stack = []
for char in input_string:
    # Thêm từng ký tự của input_string vào stack
    stack.append(char)
print('Stack sau khi thêm các ký tự:', stack)

    # Ghép thành chuỗi mới
reversed_string = ''
while len(stack) > 0:
    # Lấy từng ký tự từ stack và ghép vào reversed_string
    reversed_string += stack.pop()

print('Chuỗi sau khi đảo ngược:', reversed_string)

# Bài 3: Kiểm tra dấu ngoặc hợp lệ
# Chuỗi được gọi là hợp lệ nếu:
#     	1. Các dấu ngoặc mở và ngoặc đóng khớp với nhau đúng thứ tự: () [] {}
#     	2. Mỗi dấu ngoặc mở phải có dấu ngoặc đóng tương ứng
# Gợi ý:
#     	- Dùng stack để lưu các dấu ngoặc mở.
#     	- Khi gặp dấu ngoặc đóng, kiểm tra xem nó có khớp với dấu ngoặc mở trên cùng của stack không.
def is_valid_parentheses(s):
    stack = []
    for char in s:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if len(stack) == 0:
                return False
            top = stack.pop()
    return len(stack) == 0

str1 = "([]){}"     # True
str2 = "([))]"      # False
str3 = ")([]"       # False
print(f'Chuỗi "{str1}" hợp lệ: {is_valid_parentheses(str1)}')
print(f'Chuỗi "{str2}" hợp lệ: {is_valid_parentheses(str2)}')
print(f'Chuỗi "{str3}" hợp lệ: {is_valid_parentheses(str3)}')

# Bài 4: Đóng vai trò là 1 lập trình viên xây dựng ứng dụng web đơn giản. Hãy phát triển 2 chức năng:
# 	- Back: quay lại trang web trước đó
# 	- Forward: tiến tới trang web bạn vừa quay lại
# Yêu cầu: xây dựng lớp Browser có 3 phương thức (visit_page, back, forward)
# Gợi ý: sử dụng 2 stack để lưu lịch sử back và lịch sử forward

class Browser:
    # Hàm khởi tạo
    def __init__(self):
        # Stack lưu lịch sử web đã truy cập (back)
        self.back_stack = []
        # Stack lưu lịch sử web đã quay lại (forward)
        self.forward_stack = []

    # Phương thức truy cập website mới
    def visit_page(self, url):
        # Thêm url vào back_stack
        self.back_stack.append(url)
        # Khi truy cập trang mới, forward_stack sẽ bị xóa
        self.forward_stack.clear()
        print(f'Đang truy cập: {url}')

    # Phương thức quay lại trang web trước đó
    def back(self):
        if len(self.back_stack) > 1:
            # Lấy trang hiện tại ra khỏi back_stack và thêm vào forward_stack
            current_page = self.back_stack.pop()
            self.forward_stack.append(current_page)
            print(f'Quay lại: {self.back_stack[-1]}')
        else:
            print('Không thể quay lại, đây là trang đầu tiên!')

    # Phương thức tiến tới trang web vừa quay lại
    def forward(self):
        if len(self.forward_stack) > 0:
            next_page = self.forward_stack.pop()
            self.back_stack.append(next_page)
            print(f'Tiến tới: {next_page}')
        else:
            print('Không thể forward!')

# ------- Test ----------
    # Khởi tạo trình duyệt
browser = Browser()
    # Truy cập các trang web
browser.visit_page("www.google.com")
browser.visit_page("www.facebook.com")
browser.visit_page("www.youtube.com")
browser.visit_page("www.github.com")
browser.visit_page('www.tiktok.com')
    # Quay lại 2 lần
browser.back()
browser.back()
    # Tiến tới 1 lần
browser.forward()
print('Lịch sử back:', browser.back_stack)
print('Lịch sử forward:', browser.forward_stack)