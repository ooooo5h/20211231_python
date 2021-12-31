from models import Users

class Posts:
    
    def __init__(self, data_dict):
        self.id = data_dict['id']
        self.user_id = data_dict['user_id']
        self.title = data_dict['title']
        self.content = data_dict['content']
        self.created_at = data_dict['created_at']
        self.writer_name = data_dict['writer_name']
        
        self.reply_count = data_dict['reply_count']
        
    # 게시글 목록 표시하는 기능(간단한 정보)
    # 제목 : 실제제목 (8월 5일, 조경진이 작성함)     => 체인지 ; 작성자 이름도 같이
    def get_simple_post(self):
        
        format_date = self.created_at.strftime( '%m월 %d일' )
               
        print(f'제목 : {self.title} ({format_date}, {self.writer_name}이 작성함) - 댓글 {self.reply_count}개')
         
    