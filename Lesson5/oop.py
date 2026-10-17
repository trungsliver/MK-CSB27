import json

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []
        self.avg_grade = 0

    def add_grade(self, grade):
        if 0 <= grade <= 10:
            # Thêm điểm vào danh sách grades
            self.grades.append(grade)
            # Tính lại điểm trung bình
            self.avg_grade = self.calculate_average()
        else:
            print("Điểm không hợp lệ. Vui lòng nhập điểm từ 0 đến 10.")

    def calculate_average(self):
        if len(self.grades) > 0:
            # Tính điểm trung bình
            return sum(self.grades) / len(self.grades)
        else:
            return 0

class GradeManager:
    def __init__(self):
        self.students = []

    def add_student(self, name):
        # Kiểm tra xem học sinh đã tồn tại chưa
        for student in self.students:
            if student.name == name:
                print(f"Học sinh {name} đã tồn tại.")
                return False
        # Thêm học sinh mới vào danh sách
        new_student = Student(name)
        self.students.append(new_student)
        print(f"Đã thêm thành công học sinh {name}.")
        return True

    def record_grade(self, name, grade):
        # Tìm tên học sinh trong danh sách
        for student in self.students:
            if student.name.lower() == name.lower():
                student.add_grade(grade)
                print(f"Đã ghi nhận điểm {grade} cho học sinh {name}.")
                return True
        print(f"Học sinh {name} không tồn tại.")
        return False

    def calculate_average_all(self):
        # Kiểm tra students có học sinh nào không
        if len(self.students) == 0:
            print("Không có học sinh nào để tính điểm trung bình.")
            return
        print("\nĐiểm trung bình của từng học sinh:")
        total_avg = 0
        for student in self.students:
            total_avg += student.calculate_average()
            print(f"{student.name}: {student.calculate_average()}")
        overall_avg = total_avg / len(self.students)
        print(f"\nĐiểm trung bình chung của tất cả học sinh: {overall_avg}")

    def save_data(self, filename):
        if not filename.endswith('.json'):
            filename += '.json'
        data = []
        for student in self.students:
            student_data = {
                'name': student.name,
                'grades': student.grades,
                'avg_grade': student.avg_grade
            }
            data.append(student_data)
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
            print(f"Dữ liệu đã được lưu vào {filename}.")
        except Exception as e:
            print(f"Đã xảy ra lỗi khi lưu dữ liệu: {e}")