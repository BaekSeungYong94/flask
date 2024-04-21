#회원 가입을 위한 form을 구성하는 파일을 만듬

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField("아이디",
                           validators=[DataRequired(),Length(min=4, max=20)])
    email = StringField("이메일",
                        validators=[DataRequired(),Email()])
    password = PasswordField("비밀번호",
                             validators=[DataRequired(),Length(min=4, max=20)])
    confirm_password = PasswordField("비밀번호 확인",
                                     validators=[DataRequired(),EqualTo("password")])
    submit = SubmitField("가입")

class LoginForm(FlaskForm):
    username = StringField("아이디",
                           validators=[DataRequired(),Length(min=4,max=20)])
    password = PasswordField("비밀번호",
                             validators=[DataRequired(),Length(min=4,max=20)])
    submit = SubmitField("로그인")
    join = SubmitField("회원가입")