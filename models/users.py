# users 테이블을 표현하는 용도
# DB의 테이블을 프로그램에서 표현하는 클래스들을 model이라고 부른다

# 일시 관련 기능들이 모여있는 모듈 불러내기
import datetime

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


    # 각 사용자의 정보를 가공해서 간략하게 출력하는 기능
    # 이름 - 35세, 남성 (210805 가입)
    def get_simple_info(self):
        
        
        format_date = self.created_at.strftime('%y%m%d')
        print(f'{self.name} - {self.get_age()}세, {self.gender} ({format_date} 가입)')

    
    # 사용자의 나이 계산해주는 기능
    def get_age(self):
        
        # 오늘은 12월 31일이니까 내일부터 나이가 바껴 ㅠㅠ
        # 현재 일자의 연도를 얻어오면, 자동으로 현재 나이 계산이 가능하겠지?
        
        now_year = datetime.datetime.utcnow().year    # 세계 표준 시간(DB 기준 시간대 적용)
        return now_year - self.birth_year + 1