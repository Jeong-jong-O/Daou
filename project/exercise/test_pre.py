from flask import Flask, render_template
from flask import request
import mail

import pymysql

app = Flask(__name__)


@app.route("/login", methods = ['GET','POST'])
def view_login():
    return render_template('login.html')

@app.route("/login-test", methods = ['GET','POST'])
def id_check():
    global ID
    if request.method == 'POST':
        ID = int(request.form['login'])

    conn = pymysql.connect(host = 'localhost',
                       user = 'root',
                       password = 'root1234',
                       db = 'daou',
                       charset = 'utf8'
                       )
    
    # Cursor 생성
    cur = conn.cursor()

    sql_check = f'SELECT count(*) FROM newbie where emp_no = {ID}'
    
    cur.execute(sql_check)
    
    check_login = list(cur)[0][0]
    print(check_login)
    if check_login == 1:
        return f'\'/project/{ID}\'로 이동하세요.'
    else : 
        return '잘못된 사원번호 입니다.'         

    
        
@app.route("/project/<ID>")
def view_template(ID):
    conn = pymysql.connect(host = 'localhost',
                       user = 'root',
                       password = 'root1234',
                       db = 'daou',
                       charset = 'utf8'
                       )
    # Cursor 생성
    cur = conn.cursor()

    sql_index = 'SELECT emp_no, name, introduction, img_url FROM newbie '
    cur.execute(sql_index)
    
    check_lsts =  list(cur)
    cur.close()
    
    return render_template('index.html', ID = ID, check_lsts = check_lsts)




    

@app.route("/project/detail/<ID>/<emp_no>",methods = ['GET','POST'])
def test(ID,emp_no):
    conn = pymysql.connect(host = 'localhost',
                       user = 'root',
                       password = 'root1234',
                       db = 'daou',
                       charset = 'utf8'
                       )
    
    # Cursor 생성
    cur = conn.cursor()
    
    # DB내 newbie 테이블에서 기본 정보 가져오기
    sql_detail_index = f'SELECT name, introduction, img_url, email FROM newbie WHERE emp_no = {emp_no} '
    
    cur.execute(sql_detail_index)
    detail_lsts =  list(cur)
    name  = detail_lsts[0][0]
    intro  = detail_lsts[0][1]
    image  = detail_lsts[0][2]
    email = detail_lsts[0][3]
    
        # DB에 첫인상 멘트 저장
    sql_insert_db = 'INSERT INTO message(emp_no_send, emp_no_recieve, msg) VALUES(%s, %s, %s)'
    emp_no_recieve = emp_no
    emp_no_send = ID
    msg = '커엽다'
    msg_values = (emp_no_send, emp_no_recieve, msg)
    cur.execute(sql_insert_db, msg_values)
    conn.commit()
    
    # mail(msg, email)
    
    # DB에서 메시지 리스트 출력
    sql_msg_extract = f'SELECT msg FROM message WHERE emp_no_recieve = {emp_no}'
    cur.execute(sql_msg_extract)
    msg_lsts = list(cur)
    cur.close()
    
    return render_template("detail.html",name = name, intro = intro, image = image, msg_lsts = msg_lsts)



# def db_insert():
#     conn = pymysql.connect(host = 'localhost',
#                        user = 'root',
#                        password = 'root1234',
#                        db = 'scott',
#                        charset = 'utf8'
#                        )
#     cur = conn.cursor()
#     sql_insert_db = 'INSERT INTO message(emp_no_send, emp_no_recieve, msg) VALUES(%s, %s, %s)'
#     emp_no_send = emp_no
#     emp_no_recieve = request.args.get('recieve_id')
#     msg = request.args.get('recieve_id')
#     msg_values = (emp_no_send, emp_no_recieve, msg)
#     cur.execute(sql_insert_db, msg_values)
#     conn.commit()
#     msg_lst = []
#     sql_msg_extract = f'SELECT msg from message where emp_no_receive = {emp_no_recieve}'
#     cur.execute(sql_msg_extract)
#     for i in cur:
#         msg_lst.append(i)
#     mail(msg_lst, emp_no_recieve) 

if __name__ == "__main__":
		app.run(host = "0.0.0.0", port = 5002, debug = True)
  