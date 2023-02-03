from flask import Flask, render_template

app = Flask(__name__)

@app.route("/template-basic/<number>")  # <변수> : 경로 내 사용자가 입력하는 값을을 그대로 입력받아, html 등에 대한 변수로 사용가능 
#뷰 함수
def view_template(number):    
	title = '템플릿'
	nums_list = [1, 2, 3, 4, 5]
	nums_dict = { 'one' : 1, 'two' : 2 }
	return render_template("template.html", title = title, nums_list = nums_list, nums_dict = nums_dict)
    #render_template : 함수 내부의 데이터를 전달받아, 문서를 응답을 통해 화면에 출력하는 함수
    # (참고)왼쪽의 변수 : template 내부의 변수 , 오른쪽 변수 : 뷰함수 내부의 변수
if __name__ == "__main__":
		app.run(host = "0.0.0.0", port = 5001, debug = True)