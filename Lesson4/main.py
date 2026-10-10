import oop

# Khởi tạo Player Manager
db = oop.PlayerManager('data.json')

# Hiển thị số lượng phần tử ở 2 danh sách
print('len(db.players_dict):', len(db.players_dict))
print('len(db.players_list):', len(db.players_list))

# Chuyển từ dictionary sang object
db.dict_to_object()
print('len(db.players_dict):', len(db.players_dict))
print('len(db.players_list):', len(db.players_list))

# Thêm 1 player mới
new_player = {
    "id": 9999999,
    "name": "Thế Chương",
    "dob": "2011-06-17",
    "position": "ST",
    "region": "Russian",
    "club": "Manchester United",
    "worth": 1000
}
db.add_player(new_player)

# Test hiển thị toàn bộ player
db.show_all_players()

# Test tìm kiếm player
print(db.search_player('ro'))