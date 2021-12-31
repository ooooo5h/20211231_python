# 메뉴 입력 / 분기 처리 등 사용자 contact 부분을 전담하는 부분 


# 메인 메뉴를 출력하는 기능을 함수로 만들자
def show_main_menu():
    
    while True:
        print('===== 강의 관리 시스템 (LMS) =====')
        print('1. 수강생 목록 조회')
        print('0. 프로그램 종료')
        print('=================================')
        num = int(input('메뉴 선택 : '))
        
        if num == 0:
            print('프로그램을 종료합니다.')
            
        elif num == 1:
            # 함수의 실행은 코드를 불러낼 때 실행되는게 아니라,
            # 코드가 이미 다 불러지고, 메뉴가 다 뜨고 나서 키보드로 1번을 골랐을 때 실행됨(get_user_list_from_db함수의 호출이 완료된 시점)
            # 함수 안의 다른 함수 호출은 위아래 순서에 관계없이 불러낼 수 있다.
            get_user_list_from_db()


# 1번 : DB에서 수강생 목록 조회 요청하는 기능 추가
def get_user_list_from_db():
    print('db_handler에게 사용자 목록을 요청해야함')


# python 명령어로 실행될 때, 코드는 위에서부터 밑으로 한 줄씩 순서대로 실행
show_main_menu()