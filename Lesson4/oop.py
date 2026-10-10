import data_io

class Player: 
    def __init__(self, id, name, dob, position, region, club, worth=None):
        self.id = id
        self.name = name
        self.dob = dob
        self.position = position
        self.region = region
        self.club = club
        # Nếu có thì định dạng float, không có thì mặc định = 0
        self.worth = float(worth) if worth else 0

    def show_info(self):
        print('\n===== Player Infomation =====')
        print('ID: ', self.id)
        print('Name: ', self.name)
        print('DOB: ', self.dob)
        print('Position: ', self.position)
        print('Region: ', self.region)
        print('Club: ', self.club)
        print('Worth: ', self.worth)
        print('==============================')

    def update(self, new_data:dict):
        for key, value in new_data.items():
            # chỉ khi nào có thuộc tính thì mới gán giá trị
            if value:
                setattr(self, key, value)

class PlayerManager:
    def __init__(self, file_path):
        # file_path: đường dẫn đến file dữ liệu
        self.file_path = file_path
        # Danh sách dạng object Player
        self.players_list = list()
        # Danh sách dạng dictionary (lấy dữ liệu từ file json)
        self.players_dict = data_io.load_json_data(file_path)

    # Chuyển từ dictionary (json) sang object Player
    def dict_to_object(self):
        new_players = []
        for player in self.players_dict:
            # Lấy thông tin từ json để tạo object Player
            obj_player = Player(id = player["id"],
                                name = player["name"],
                                dob = player["dob"],
                                position = player["position"],
                                region = player["region"],
                                club = player["club"],
                                worth = player["worth"])
            new_players.append(obj_player)
        # Gán danh sách sau chuyển đổi vào thuộc tính players_list
        self.players_list = new_players

    # Chuyển từ object Player sang dictionary (json)
    def object_to_dict(self):
        json_data = list()
        for player in self.players_list:
            # __dict__: hàm có sẵn, convert obj -> dict
            dict_player = player.__dict__
            json_data.append(dict_player)
        # Ghi dữ liệu vào file json
        data_io.write_json_data(self.file_path, json_data)
        return json_data

    # Hiển thị toàn bộ thông tin player
    def show_all_players(self):
        for player in self.players_list:
            # Sử dụng method show_info() của class Player 
            player.show_info()

    # Thêm 1 player mới
    def add_player(self, new_player:dict):
        # ID của player mới
        new_player["id"] = len(self.players_dict) + 1
        # Thêm player mới vào danh sách dict
        self.players_dict.append(new_player)
        # Chuyển sang object Player và thêm vào danh sách object
        self.dict_to_object()
        # Ghi dữ liệu vào file json
        data_io.write_json_data(self.file_path, self.players_dict)

    # Tìm 1 player theo ID
    def find_player_by_id(self, player_id:int):
        for player in self.players_list:
            if player.id == player_id:
                return player
        return None

    # Sửa thông tin player theo ID
    def update_player(self, player_id:int, new_data:dict):
        # Tìm player theo ID
        player = self.find_player_by_id(player_id)
        if player:
            # Cập nhật thông tin player
            player.update(new_data)
            # Chuyển sang dict và ghi dữ liệu vào file json
            self.object_to_dict()
            # Ghi dữ liệu vào players_list
            self.dict_to_object()
            return True
        return False

    # Xóa player theo ID
    def delete_player(self, player_id:int):
        # Tìm player theo ID
        player = self.find_player_by_id(player_id)
        if player:
            # Xóa player khỏi danh sách object
            self.players_list.remove(player)
            # Chuyển sang dict và ghi dữ liệu vào file json
            self.object_to_dict()
            # Ghi dữ liệu vào players_list
            self.dict_to_object()
            return True
        return False

    # Tìm danh danh sách player mà tên có chứa chuỗi tìm kiếm
    def search_player(self, search_name):
        # Danh sách lưu kết quả (dạng object)
        matched_players = []
        for player in self.players_list:
            if search_name.lower() in player.name.lower():
                matched_players.append(player.__dict__)
        return matched_players