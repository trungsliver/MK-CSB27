import json

students = [
    {
        "name": "Tiến Dũng",
        "age": 14,
        "gender": "male"
    },
    {"name": "Ngọc Huy", "age": 15, "gender": "male"},
    {"name": "Minh Ngọc", "age": 14, "gender": "female"}
]

# Ghi nội dung vào file json
with open("data.json", "w", encoding="utf-8") as f:
    # indent=4: định dạng giúp file dễ đọc
    # ensure_ascii=False: để giữ nguyên ký tự Unicode (giữ nguyên tiếng việt)
    json.dump(students, f, indent=4, ensure_ascii=False)

# Đọc nội dung từ file JSON
with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)
print(data)