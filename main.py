# 사용자에게 보여지는 부분 전담 => View
# Model + Controller + View 조합해서 코딩하는 패턴을 MVC 패턴이라고 함


# 메뉴 입력 / 분기 처리 등 사용자 contact 부분을 전담하는 부분 
from db_handler import get_user_list, get_posts
from models import Users
from models.posts import Posts

# 메인 메뉴를 출력하는 기능을 함수로 만들자
def show_main_menu():
    
    while True:
        print('===== 강의 관리 시스템 (LMS) =====')
        print('1. 수강생 목록 조회')
        print('2. 게시글 목록 조회')
        print('0. 프로그램 종료')
        print('=================================')
        num = int(input('메뉴 선택 : '))
        
        if num == 0:
            print('프로그램을 종료합니다.')
            break
            
        elif num == 1:
            # 함수의 실행은 코드를 불러낼 때 실행되는게 아니라,
            # 코드가 이미 다 불러지고, 메뉴가 다 뜨고 나서 키보드로 1번을 골랐을 때 실행됨(get_user_list_from_db함수의 호출이 완료된 시점)
            # 함수 안의 다른 함수 호출은 위아래 순서에 관계없이 불러낼 수 있다.
            get_user_list_from_db()

        elif num == 2:
            # DB에서 게시글 목록 조회 요청
            page_num = int(input('몇 페이지의 글을 보겠습니까? : '))
            get_posts_by_page_num(page_num)

# 1번 : DB에서 수강생 목록 조회 요청하는 기능 추가
def get_user_list_from_db():
    
    result = get_user_list()   # DB 전담 클래스가 보내준 결과(dict여러개를 tuple로)를 , UI(main.py)에서 활용하기
    
    # for문으로 돌면서 문구가공 및 출력
    for row in result:
        # print(row)    # row한줄이 dict로 표현됨
        user = Users(row)
        user.get_simple_info()   # user에 만들어진 메쏘드를 활용
    

# 2번 : DB에서 게시글을 요청한 페이지에 맞게 요청하는 기능 추가
def get_posts_by_page_num(page):
    result = get_posts(page)
    
    for row in result:
        post = Posts(row)
        print(post.title)
    

# python 명령어로 실행될 때, 코드는 위에서부터 밑으로 한 줄씩 순서대로 실행
show_main_menu()