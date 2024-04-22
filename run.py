from flask import Flask, render_template, url_for, flash, redirect, request
from forms import RegistrationForm,LoginForm,MainForm
import secrets
app = Flask(__name__)

#CSRF(Cross-Site Request Forgery)
#form으로 전송된 데이터가 실제 웹 페이지에서 작성된 데이터인지를 판단해주는 가늠자 역할
app.config["SECRET_KEY"] = secrets.token_hex(16)

#데이터를 변수로 대체
title_list = {
        1:{"title":"hi","text":"반가워요"},
        2:{"title":"hello","text":"hello world"}
    }

#@ 데코레이터
#@로 시작하며 함수를 수정하지 않은 상태에서 추가 기능을 구현할 때 사용
#첫 페이지는 로그인 페이지로 만들었고 로그인,회원가입을 위해 method 지정
@app.route('/',methods=["GET","POST"])
def login():
    form = LoginForm()
    #join이라는 name을 가지고 있는 input의 입력값을 가져온다.
    print (request.args.get('join'))
    
    return render_template('login.html',form=form)

#회원가입 시 성공 메세지를 출력하기 위한 페이지(최상위 페이지)
@app.route('/')
def home():
    return render_template('layout.html')

#회원가입 페이지
#회원가입 정보를 DB에 저장하기 위한 코드 추가 예정
@app.route('/register', methods=["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        #flaskform의 데이터 가져오기
        username = request.form['username']
        password2 = request.form['password']
        email2 = request.form['email']

        print (username,password2,email2)
        flash(f'{form.username.data}님 가입 완료!','success')
        return redirect(url_for('home'))
    return render_template('register.html',form=form)

#로그인 후 메인 페이지
@app.route('/main',methods=["POST"])
def main():
    form = MainForm()
       
    return render_template('main.html',form=form,title=title_list)

#게시글 페이지
@app.route('/post/<int:id>',methods=["GET"])
def post(id):
    return render_template('post.html',data=title_list[id]["text"])

if __name__ == "__main__":  
    app.run(debug=True)