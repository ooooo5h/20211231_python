# DB 연결 / 쿼리 / 결과 분석 표시 등등
# DB 관련된 파이썬 코드 작성 부분   
from pymysql import connect
from pymysql import cursors
from pymysql.cursors import DictCursor   # DictCursor : DB SELECT 결과를 dict 형태로 가져오게 해주는 클래스

# connect함수를 직접 import해서, ' pymysql. ' 이라는 코드 생략
db = connect(
    host = 'finalproject.cbqjwimiu76h.ap-northeast-2.rds.amazonaws.com',
    port = 3306,   # port? : 한 대의 컴퓨터가 여러개의 프로그램을 돌릴 때, 각각의 프로그램(mysql은 3306 포트에 실행시키는 게 일반적)을 찾아갈 때(=인터넷을 통해) 사용하는 고유번호        
    user = 'admin',
    passwd = 'Vmfhwprxm!123',   
    db = 'test_202112_python',   # host에 만들어져있는 많은 논리DB 中 사용할 DB를 선정하는 작업
    charset = 'utf8',   # 연결할 DB가 utf8 인코딩으로 한글 처리를 진행
    cursorclass = DictCursor
)

# 쿼리수행을 전담하는 변수 생성(어디서? 연결된 DB에서 수행)
cursor = db.cursor()

# 연결 확인용 SELECT문 날려보자

# sql문 작성
# cursor.execute
# 결과 fetch를 list/dict 등의 형태로 변환
sql= 'SELECT * FROM users'
cursor.execute(sql)
result = cursor.fetchall()
print(result)