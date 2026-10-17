import oop

manager = oop.GradeManager()

while True:
    print("\n--- Quản lý điểm học sinh ---")
    print("1. Thêm học sinh")
    print("2. Ghi nhận điểm cho học sinh")
    print("3. Tính điểm trung bình của từng học sinh")
    print("4. Lưu dữ liệu")
    print("5. Thoát")
    print("-------------------------------")

    choice = input("Chọn một tùy chọn (1-5): ")

    if choice == "1":
        name = input("Nhập tên học sinh: ")
        manager.add_student(name)
    elif choice == "2":
        name = input("Nhập tên học sinh: ")
        try:
            grade = float(input("Nhập điểm (0-10): "))
            manager.record_grade(name, grade)
        except ValueError:
            print("Điểm không hợp lệ. Vui lòng nhập một số từ 0 đến 10.")
    elif choice == "3":
        manager.calculate_average_all()
    elif choice == "4":
        filename = input("Nhập tên file để lưu dữ liệu: ")
        manager.save_data(filename)
    elif choice == "5":
        print("Thoát chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")