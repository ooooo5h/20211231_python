# users 테이블을 표현하는 용도
# DB의 테이블을 프로그램에서 표현하는 클래스들을 model이라고 부른다

class Users:
    
    def __init__(self, info_dict):
        # info_dict안의 이름표와 실제 값을 이용해서 데이터를 세팅해보자
        self.id = info_dict['id']
        self.name = info_dict['name']
        self.birth_year = info_dict['birth_year']
        self.address = info_dict['address']
        self.gender = info_dict['gender']
        self.height = info_dict['height']
        self.created_at = info_dict['created_at']
        self.friend_id = info_dict['friend_id']
        
        