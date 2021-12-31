# DB를 조회 + 수정 + 추가 등의 작업들을 하는 공간 : DB를 제어한다(control)
# 모델을 이용해서 데이터를 컨트롤한다 => Controller

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

# 필요 기능들을 함수로 작성
# 1. 수강생 목록조회
def get_user_list():
    
    sql = f"SELECT * FROM users"
    
    cursor.execute(sql)
    result = cursor.fetchall()
    
    # API => 원하는 쿼리의 수행 결과를 잘 가공해서, 화면단에서 사용할 수 있게 전달해주는 역할
    return result


# 2. 페이지에 맞는 게시글 목록 조회
def get_posts(page):
    # 1페이지당 5개의 글을 보여준다.
    # 1페이지 : 0개의 글 pass, 그 다음 5개(1~5)
    # 2페이지 : 5개의 글 pass, 그 다음 5개(6~10)
    # 3페이지 : 10개의 글 pass, 그 다음 5개의 글 (11~15)
    
    
    # ORDER BY / LIMIT 쿼리 활용해보자
    # LIMIT 건너뛸 갯수 : 5개, 보여줄 갯수 : 5개
    
    # 몇 페이지냐에 따라 건너뛸 갯수는 몇개? 
    offset = (page - 1) * 5
    sql = f"SELECT * FROM posts AS p ORDER BY p.created_at DESC LIMIT {offset}, 5"
    
    cursor.execute(sql)
    result = cursor.fetchall()

    return result