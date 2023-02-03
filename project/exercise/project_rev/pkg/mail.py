from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib 

def mail(message, receiver) :
    SMTP_SERVER = 'smtp.gmail.com'
    SMTP_PORT = 465
    SMTP_USER = 'daou.icebreaking@gmail.com'
    SMTP_PASSWORD = 'rzlxbyvddgjanpjt'
    
    # 기본 내용 및 구조
    msg = MIMEMultipart('alternative')
    msg['From'] = SMTP_USER
    msg['To'] = receiver
    msg['Subject'] = '[다우기술] 첫인상 메세지'
    
    text = MIMEText(message, _charset='utf-8')
    msg.attach(text)
        
    # 실제 메일 보내는 코드
    smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
    smtp.login(SMTP_USER, SMTP_PASSWORD)
    smtp.sendmail(SMTP_USER, receiver, msg.as_string())
    smtp.close()