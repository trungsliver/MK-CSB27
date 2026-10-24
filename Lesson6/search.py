# ============== THUẬT TOÁN TÌM KIẾM ==============
arr = [2, 5, 3, 1, 9, 7, 4, 8, 6]

# Tìm kiếm tuyến tính / tuần tự (Linear Search)
def linear_search(arr, target):         # O(n)
    # Duyệt từng phần tử trong danh sách
    for i in range(len(arr)):
        if arr[i] == target:
            return i    # Trả về vị trí của phần tử nếu tìm thấy
    return -1           # Trả về -1 nếu không tìm thấy

print("Kết quả tìm kiếm tuyến tính:", linear_search(arr, 7))  # Output: 5

# Tìm kiếm nhị phân (Binary Search)
    # Lưu ý: Danh sách cần được sắp xếp trước
def binary_search(arr, target):         # O(log n)
    # left, right chỉ số index bắt đầu và kết thúc (chặn đầu và chặn cuối)
    left = 0
    right = len(arr) - 1

    while left <= right:  
        # Tìm chỉ số index của phần tử ở giữa
        mid = (left + right) // 2
        # So sánh phần tử ở giữa với target
        if arr[mid] == target:
            return mid    # Trả về vị trí của phần tử nếu tìm thấy
        elif arr[mid] < target:
            left = mid + 1  # Tìm kiếm nửa bên phải
        else:
            right = mid - 1  # Tìm kiếm nửa bên trái
    return -1  # Trả về -1 nếu không tìm thấy