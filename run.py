from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm,LoginForm
import secrets
app = Flask(__name__)

#CSRF(Cross-Site Request Forgery)
app.config["SECRET_KEY"] = secrets.token_hex(16)

@app.route('/')
def login():
    form = LoginForm()
    return render_template('login.html',form=form)

def home():
    return render_template('layout.html')

@app.route('/register', methods=["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'{form.username.data}님 가입 완료!','success')
        return redirect(url_for('home'))
    return render_template('register.html',form=form)

if __name__ == "__main__":  
    app.run(debug=True)