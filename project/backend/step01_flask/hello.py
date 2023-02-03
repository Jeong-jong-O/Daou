from flask import Flask
from flask import request

# 플라스크 객체 생성
app = Flask(__name__)   # __name__ : 자신의 모듈을 지칭함 (여기서는 hello) -> python  명령어로 실행되면 main으로 변경됨. 

# 서버 구동시, 개발 정의 URL값과 플라스크에서 정의된 함수를 연결
@app.route("/hello")    # route : 서버 url을 설정하여, 서비스에 대한 접속을 가능케 함. 
def hello_flask():      # 해당 경로로 들어왔을 때 실행해야 할 함수인 뷰 함수를 설정
		return "SOS"

@app.route("/login", methods=['GET', 'POST'])
def print_id_pw():
  if request.method == 'GET':
    print('GET Method')
    id = request.args.get('id')
    pw = request.args.get('pw')
  elif request.method == 'POST':
    print('POST Method')
    id = request.form['id']
    pw = request.form['pw']
  return id + ' ' + pw

# 해당 파일 실행시 플라스크 서버 실행   
if __name__ == "__main__":  # name이 main이면 = 실행이 되면
		app.run(host = "0.0.0.0", port = 5000, debug = True)    # Flask가 돌아가는 서버