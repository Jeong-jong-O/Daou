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
    
    text_body = f'''
    <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="https://jeong-jong-o.github.io/Icebreaking/css/style.css">
            <link rel="stylesheet" href="https://jeong-jong-o.github.io/Icebreaking/css/email.css">
            <title>DAOU人</title>
        </head>
        <body>
            <br/>
            <br/>
            <br/>
            <br/>
            <br/>
            <br/>
            <br/>
            <div class="login">
                <h1 class="login-title">
                    <img src="https://github.com/Jeong-jong-O/Icebreaking/blob/main/img/daou_logo.png?raw=true" alt="daou_logo" class="login-logo" />
                    <span class="login-description">끊임없는 변화와 혁신을 추구하는 다우기술입니다.</span>
                </h1>

                <span class="email-title">받은 첫인상 메세지</span>
                <p class="msg">{message}</p>
            </div>
        </body>
    </html>
    '''
        
    text = MIMEText(text_body, 'html')
    msg.attach(text)
    
    # 실제 메일 보내는 코드
    smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
    smtp.login(SMTP_USER, SMTP_PASSWORD)
    smtp.sendmail(SMTP_USER, receiver, msg.as_string())
    smtp.close()