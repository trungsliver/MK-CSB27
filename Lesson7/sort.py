arr = [64, 25, 12, 22, 11, 90, 34, 78, 56, 43]

# ============ SELECTION SORT ============

    # Cách 1 (slide MindX)
def selection_sort_1(arr:list):     # Độ phức tạp: O(n^2)
    # Tạo danh sách rỗng
    arr_sorted = []
    while len(arr) > 0:
        # Tìm phần tử lớn nhất
        max_value = max(arr)
        # Thêm phần tử lớn nhất vào danh sách rỗng
        arr_sorted.append(max_value)
        # Xóa phần tử lớn nhất khỏi danh sách ban đầu
        arr.remove(max_value)
    return arr_sorted

print("Selection Sort 1:", selection_sort_1(arr.copy()))

    # Cách 2 (video youtube)
def selection_sort_2(arr:list):     # Độ phức tạp: O(n^2)
    # Duyệt toàn bộ danh sách
    for i in range(len(arr)):
        # Giả sử min_index nầm tại i
        min_index = i
        # Tìm phần tử nhỏ nhất trong phần còn lại
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        # Đổi chỗ arr[i] và arr[min_index]
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
print("Selection Sort 2:", selection_sort_2(arr.copy()))

# ============== BUBBLE SORT ==============
def bubble_sort(arr:list):      # Độ phức tạp: O(n^2)
    # Duyệt danh sách
    for i in range(len(arr)):
        # So sánh các phần tử cạnh nhau
        for j in range(0, len(arr) - i - 1):
            # Nếu phần tử trái > phải, hoán đổi vị trí
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print("Bubble Sort:", bubble_sort(arr.copy()))

# =============== INSERTION SORT ================
    # Giống xếp bài tú lơ khơ trên tay
def insertion_sort(arr):        # Độ phức tạp: O(n^2)
    # Duyệt từ phần tử thứ hai đến phần tử cuối cùng
    for i in range(1, len(arr)):
        # Phần tử cần chèn
        key = arr[i]
        # So sánh key với các phần tử trước nó  
        j = i - 1
        # Dịch chuyển các phần tử lớn hơn key về bên phải
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        # Chèn key vào vị trí đúng
        arr[j + 1] = key
    return arr

print("Insertion Sort:", insertion_sort(arr))