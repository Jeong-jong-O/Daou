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
            # 로그인 페이지에서 사원번호를 전달받는다면, 해당 사원번호를 ID로 저장한 이후 해당 ID를 유지하기 위해 세션에 저장
            ID = request.form['login']
            session['emp_no'] = ID
        else:
            # 로그인 페이지에서 사원번호를 전달받지 않는 경우(개별 사원에서 전체 사원으로 넘어가는 경우), 세션에 저장된 사원번호를 ID에 저장
            ID = session['emp_no']
        conn = pymysql.connect(host = 'localhost',
                        user = 'root',
                        password = 'root1234',
                        db = 'daou',
                        charset = 'utf8'
                        )
        
        cur = conn.cursor()
        
        sql_check = f'SELECT count(*) FROM newbie where emp_no = {ID}'
        cur.execute(sql_check)
        check_login = list(cur)[0][0]
        
        if check_login == 1:
        # 세션에 저장된 ID가 신입사원(newbie) 테이블에 저장되어 있는 경우, 해당 사원에 대한 정보를 index.html에 전달
            conn = pymysql.connect(host = 'localhost',
                        user = 'root',
                        password = 'root1234',
                        db = 'daou',
                        charset = 'utf8'
                        )

            cur = conn.cursor()

            sql_index = 'SELECT emp_no, name, introduction, img_url FROM newbie '
            cur.execute(sql_index)
            
            check_lsts =  list(cur)
            
            sql_login_user = f'SELECT name FROM newbie WHERE emp_no={ID}'
            cur.execute(sql_login_user)
            user_name = list(cur)[0][0]
            
            sql_comment_lst = f'SELECT emp_no_recieve FROM (SELECT * FROM message WHERE emp_no_send = {ID}) as table1'
            cur.execute(sql_comment_lst)
            comment_lst = list(cur)
            comment_emp_no_set = set()
            for i in comment_lst:
                comment_emp_no_set.add(i[0])
            comment_emp_no_set.add(int(ID))
            
            entire_emp_no_set = set()
            for i in check_lsts:
                entire_emp_no_set.add(i[0])
            emp_no_nonmentioned_lst = list(entire_emp_no_set - comment_emp_no_set)
            
            emp_name_nonmetioned_lst = []
            for i in emp_no_nonmentioned_lst:
                sql_nonmentioned_name = f'SELECT name FROM newbie where emp_no = {i}'
                cur.execute(sql_nonmentioned_name)
                emp_name_nonmetioned_lst.append(list(cur)[0])
            
            name_nonmentioned_lsts = list()
            for i in emp_name_nonmetioned_lst:
                name_nonmentioned_lsts.append(i[0])
            
            print(name_nonmentioned_lsts)

            return render_template('index.html', ID = session['emp_no'], user_name = user_name, check_lsts = check_lsts, name_nonmentioned_lsts = name_nonmentioned_lsts)
        
        else :
        # 세션에 저장된 ID가 신입사원(newbie) 테이블에 저장되어 있지 않은 경우, 잘못된 사원번호라는 오류메시지를 login.html에 전달
            return render_template('login.html', caution_msg ='잘못된 사원번호입니다. 사번을 다시 입력해 주세요.')
    else :
        # login 창에 아무것도 입력하지 않은 경우, 사번을 입력해달라는 메시지를 login.html에 전달
        return render_template('login.html', caution_msg ='입력창에 사번을 입력해주세요.')



@app.route("/detail/<emp_no>",methods = ['GET','POST'])
def test(emp_no):
    
    conn = pymysql.connect(host = 'localhost',
                        user = 'root',
                        password = 'root1234',
                        db = 'daou',
                        charset = 'utf8'
                        )
    
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
    
    # 개별 사원페이지에서 DB 내 해당 사원에 대한 메시지 리스트 출력
    sql_msg_extract = f'SELECT msg FROM message WHERE emp_no_recieve = {emp_no}'
    cur.execute(sql_msg_extract)
    msg_lsts = list(cur)
    
    # DB에 작성한 첫인상 멘트 저장
    sql_insert_db = 'INSERT INTO message(emp_no_send, emp_no_recieve, msg) VALUES(%s, %s, %s)'
    emp_no_recieve = emp_no
    emp_no_send = session['emp_no']
    global msg
    
    # 접속한 아이디와 메세지 수신자가 동일한 경우 메세지 남기기 불가
    if ID == emp_no_recieve :
        return render_template("detail.html", name = name, emp_no = emp_no, intro = intro, image = image, msg_lsts = msg_lsts,user_name = user_name, ID = session['emp_no'], caution_msg ='자신한테 메시지를 보낼 수 없습니다.')
    
    # 한 사원이 같은 사원에게 한 개의 메시지만 전달할 수 있도록 설정
    sql_check_dup = f'SELECT COUNT(*) FROM message where emp_no_recieve = {emp_no_recieve} and emp_no_send = {ID}'
    cur.execute(sql_check_dup)
    msg_cnt = int(list(cur)[0][0])

    if msg_cnt >= 1 :
        # DB 내 현재 접속한 ID의 사원번호가 해당 사원에게 메시지를 보낸 이력이 있을 경우, 첫인상 메시지를 두 개 이상 보낼 수 없다는 경고메시지를 detail.html에 전달
        return render_template("detail.html", name = name, emp_no = emp_no, intro = intro, image = image, msg_lsts = msg_lsts,user_name = user_name, ID = session['emp_no'], caution_msg ='메시지는 한 번만 남길 수 있습니다.')
    
    elif request.form.get("message") != "" :
        # 입력한 메시지가 개별 사원 리스트에 바로 반영되도록 설정
        if request.method == 'POST':
            msg = request.form['message']
            msg_values = (emp_no_send, emp_no_recieve, msg)
            cur.execute(sql_insert_db, msg_values)
            conn.commit()
            cur.execute(sql_msg_extract) 
            msg_lsts = list(cur)
    
            mail(msg, email)
            
        return render_template("detail.html",name = name, emp_no = emp_no, intro = intro, image = image, msg_lsts = msg_lsts,user_name = user_name, ID = session['emp_no'])
    else :
        # 입력하지 않은 경우, 개별 사원에 대한 메시지를 입력해달라는 메시지를 detail.html에 전달
        return render_template("detail.html", name = name, emp_no = emp_no, intro = intro, image = image, msg_lsts = msg_lsts,user_name = user_name, ID = session['emp_no'], caution_msg ='첫인상 메세지를 입력해 주세요.')


if __name__ == "__main__":
		app.run(host = "0.0.0.0", port = 5002, debug = True)
