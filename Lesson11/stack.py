# ================ STACK - Ngăn Xếp ==================

# Khái niệm: cấu trúc dữ liệu
# Nguyên tắc hoạt động: LIFO (Last In First Out) - Vào sau ra trước

# Ví dụ:
    # Xếp đĩa chồng lên nhau
    # Lịch sử trình duyệt (khi ấn back lần đầu tiên, trở về website cuối cùng đã truy cập)

# Các thao tác cơ bản:
    # Create: tạo stack
stack = []
stack1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # push/append: thêm phần tử vào stack
stack.append(1)
stack.append(2)
stack.append(3)
print('Sau khi thêm:', stack)  

    # pop: loại bỏ phần tử khỏi stack và trả về phần tử đó
stack.pop()
print('Sau khi xóa:', stack)  

top_element = stack.pop()
print('Phần tử vừa xóa:', top_element)
print('Sau khi xóa:', stack)  

    # peek: Xem phần tử ở đỉnh stack (không xóa)
top_element = stack1[-1]  # hoặc stack[len(stack) - 1]
print('Phần tử ở đỉnh stack:', top_element)

    # is_empty: kiểm tra stack có rỗng hay không
def is_empty(stack):
    return len(stack) == 0
print('Stack có rỗng không?', is_empty(stack))
print('Stack1 có rỗng không?', is_empty(stack1))    