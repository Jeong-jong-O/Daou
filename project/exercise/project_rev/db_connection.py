from flask import Flask, render_template
from flask import request,session
import pymysql
from pkg.mail import mail

app = Flask(__name__)
app.secret_key = "Daou"

@app.route("/", methods = ['GET','POST'])
def view_login():
    return render_template('login.html')


    

@app.route("/project", methods = ['GET','POST'])
def id_check():
    if request.form.get("login") != "" :
        if request.method == 'POST':
            ID = request.form['login']
            session['emp_no'] = ID
        else:
            ID = session['emp_no']
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
            
            sql_login_user = f'SELECT name FROM newbie WHERE emp_no={ID}'
            cur.execute(sql_login_user)
            user_name = list(cur)[0][0]
            
            cur.close()
            
            return render_template('index.html', ID = session['emp_no'], user_name = user_name, check_lsts = check_lsts)
        else : 
            return render_template('login.html', caution_msg ='잘못된 사원번호입니다. 사번을 다시 입력해 주세요.')  
    else :
        return render_template('login.html', caution_msg ='입력창에 사번을 입력해주세요.')  



@app.route("/detail/<emp_no>",methods = ['GET','POST'])
def test(emp_no):
    conn = pymysql.connect(host = 'localhost',
                        user = 'root',
                        password = 'root1234',
                        db = 'daou',
                        charset = 'utf8'
                        )
    
    # Cursor 생성
    cur = conn.cursor()
    
    ID = session['emp_no']
    sql_login_user = f'SELECT name FROM newbie WHERE emp_no={ID}'
    cur.execute(sql_login_user)
    user_name = list(cur)[0][0]
    
    # DB내 newbie 테이블에서 기본 정보 가져오기
    sql_detail_index = f'SELECT name, introduction, img_url, email FROM newbie WHERE emp_no = {emp_no} '
    
    cur.execute(sql_detail_index)
    detail_lsts =  list(cur)
    name  = detail_lsts[0][0]
    intro  = detail_lsts[0][1]
    image  = detail_lsts[0][2]
    email  = detail_lsts[0][3]
    
    # DB에서 메시지 리스트 출력
    sql_msg_extract = f'SELECT msg FROM message WHERE emp_no_recieve = {emp_no}'
    cur.execute(sql_msg_extract)
    msg_lsts = list(cur)
    
    # DB에 첫인상 멘트 저장
    sql_insert_db = 'INSERT INTO message(emp_no_send, emp_no_recieve, msg) VALUES(%s, %s, %s)'
    emp_no_recieve = emp_no
    emp_no_send = session['emp_no']
    global msg
    
    if request.form.get("message") != "" :
        if request.method == 'POST':
            if ID == emp_no_recieve:
                print('자신한테 메시지를 보낼 수 없습니다.')
            else:                
                sql_check_dup = f'SELECT COUNT(*) FROM message where emp_no_recieve = {emp_no_recieve}'
                cur.execute(sql_check_dup)
                msg_cnt = int(list(cur)[0][0])
                if msg_cnt >=1 :
                    print('메시지 두번 보낼 수 없습니다.')
                else:
                    msg = request.form['message']
                    msg_values = (emp_no_send, emp_no_recieve, msg)
                    cur.execute(sql_insert_db, msg_values)
                    conn.commit()
                    cur.execute(sql_msg_extract) 
                    msg_lsts = list(cur)
            
                    # mail(msg, email)
            
        return render_template("detail.html",name = name, emp_no = emp_no, intro = intro, image = image, msg_lsts = msg_lsts,user_name = user_name, ID = session['emp_no'])
    else :
        return render_template("detail.html", name = name, emp_no = emp_no, intro = intro, image = image, msg_lsts = msg_lsts,user_name = user_name, ID = session['emp_no'], caution_msg ='첫인상 메세지를 입력해 주세요.')


if __name__ == "__main__":
		app.run(host = "0.0.0.0", port = 5002, debug = True)
