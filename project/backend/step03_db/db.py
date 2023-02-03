from flask import Flask, render_template
from flask import request

import pymysql

app = Flask(__name__)

@app.route("/db")   
    #뷰 함수
def view_template():
	return render_template('db.html')
    #render_template : 함수 내부의 데이터를 전달받아, 문서를 응답을 통해 화면에 출력하는 함수
        # (참고)왼쪽의 변수 : template 내부의 변수 , 오른쪽 변수 : 뷰함수 내부의 변수

@app.route("/dept-search")

def search_dept():
    dept_no = request.args.get('deptno')
    print(dept_no)
    print('----')
    # DB 연결    
    conn = pymysql.connect(host = 'localhost',
                       user = 'root',
                       password = 'root1234',
                       db = 'scott',
                       charset = 'utf8'
                       ) 

    # 2. DB 내 커서(cursor ; 작업을 수행하고 결과값을 보유하는 객체) 생성
    cur = conn.cursor()
    
    sql_1 = f'select * from emp where deptno ={dept_no}'
    cur.execute(sql_1)

    result = []
    
    for record in cur : 
        result.append([record[0],record[1]])
        print(record[0],record[1])
    print('--------------------------------------------')
    
    
    return render_template('result.html',result = result)

if __name__ == "__main__":
		app.run(host = "0.0.0.0", port = 5002, debug = True)