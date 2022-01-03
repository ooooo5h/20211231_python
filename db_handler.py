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
    sql = f"SELECT p.*, u.name AS writer_name FROM posts AS p JOIN users AS u ON p.user_id = u.id ORDER BY p.created_at DESC LIMIT {offset}, 5"
    
    cursor.execute(sql)
    result = cursor.fetchall()
    
    for row in result:
        
        # print(row)   # 5개의 딕셔너리가 나옴  => 게시글에 대한 정보(posts테이블)를 담은 dict였음
        # row는 dict로 구성되어있고, 새로운 키와 새로운 값을 대입할 수 있겠네?
        # 결과로 나가기 전에, 각 줄의 dict를 수정해서 내보내주자(각 게시물별로 쿼리를 재수행하자 댓글의 갯수를 COUNT로)
        row['reply_count'] = 0
        
        
        # 각 게시글 별 쿼리 수행 (댓글 몇개?)
        sql = f"""
        SELECT COUNT(*) AS reply_count
        FROM posts_reply AS pr
        WHERE pr.post_id = {row['id']}
        """
        
        cursor.execute(sql)
        reply_count_result = cursor.fetchone()
        # print(reply_count_result)   # dict형태로 받아온 결과가 출력
        row['reply_count'] = reply_count_result['reply_count']
        
    return result


# 3. DB에 모든 회원의 수를 물어보는 함수 추가
def get_all_user_count():   # 결과 자체를 숫자로 리턴해주면 편하겠지?
    
    sql = f"SELECT COUNT(*) AS user_count FROM users"
    
    cursor.execute(sql)
    result = cursor.fetchone()    # 목록말고, 최초의 한 줄만 가져와라(어차피 한줄뿐일테니까)
    
    return result['user_count']


# 4. DB에 강의목록과 평점을 같이 가져오는 함수 추가
def get_all_lectures():
    
    # 강의 목록(SELECT) / 집계 함수 (GROUP BY) 활용 예시
    sql = f"""
    SELECT l.id, l.name 
    FROM lectures AS l;
    """          # """  여러줄의 str을 쉽게 작성할 수 있게 도와주는 tool  """
    
    cursor.execute(sql)
    result = cursor.fetchall()
    
    for row in result:
        
        row['avg_score'] = 0
        
        sql = f"""
        SELECT l.name , ROUND(AVG(lr.score), 1) AS avg_score
        FROM lectures AS l
        JOIN lecture_review AS lr ON l.id = lr.lecture_id
        WHERE l.id = {row['id']};   
        """
    
        cursor.execute(sql)
        result_with_score = cursor.fetchone()
        
        if result_with_score['avg_score'] == None:
            row['avg_score'] = f'0'
        else:
            row['avg_score'] = result_with_score['avg_score']
    
    return result


# DB에 강의 추가하기 (INSERT INTO)
def add_lecture(name, max_count, fee, campus):
    sql = f"INSERT INTO lectures (lectures.name, lectures.max_count, lectures.fee, lectures.campus) VALUES ('{name}', {max_count}, {fee}, '{campus}') "   # INSERT INTO, 입력받은 항목들을 쿼리날리기
    
    cursor.execute(sql)  # DB에 쿼리 수행 준비( 변동사항은 commit으로 확정을 지어야 DB에 기록이 된다)
    db.commit()