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