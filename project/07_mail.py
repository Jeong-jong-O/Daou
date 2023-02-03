#####################
## 자동 메일 보내기 ##
#####################


from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart  # 전송된 텍스트 등의 자원이 바이너리 형태 등으로 변환시켜주는 모듈
import smtplib

# 메일 보내는 과정 : 사용자 - (SMTP) -> 서버 -(POP)-> qㅏㄷ는 사람 
# 메일을 보내기 위해 필요한 정보 : SMTP, POP, 계정의 정보
    # SMTP : 보내는 메일
    # POP : 받는 메일
    # 계정의 정보

# 환경변수
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 465 #메일서비스의 고유한 포트 정보
SMTP_USER = 'wjdwhddh307@gmail.com'
SMTP_PASSWORD = 'xuhdndkdsvuetbfk'

# 기본 내용의 주소
msg = MIMEMultipart('alternative')  # 첨부파일이 있을 경우의 옵션은 'mixed' => 나머지들은 기본적으로 'alternative'

# 키값은 서버 내에서 정해짐
msg['From'] = SMTP_USER
msg['To'] = SMTP_USER
msg['Subject'] ='자동 메일 보내기'

text = MIMEText('연휴 개꿀', _charset = 'utf-8' )  # _charset : 인코딩 방식
msg.attach(text)



# 실제 메일을 보내는 코드
smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) # 서버 빌림
smtp.login( SMTP_USER, SMTP_PASSWORD )             # 로그인
smtp.sendmail(from_addr = SMTP_USER, to_addrs = SMTP_USER, msg = msg.as_string())
smtp.close()
