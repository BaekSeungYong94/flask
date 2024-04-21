from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return 'hello home'

@app.route('/user/<user_name>/<int:user_id>')
def user(user_name,user_id):
    #return 'hello user'
    return f'Hello, {user_name}({user_id})!'

if __name__ == "__main__":
    app.run(debug=True)