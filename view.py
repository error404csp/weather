from flask import Flask, redirect, url_for, render_template, request, session, flash
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import UserMixin

db = SQLAlchemy()
DB_NAME = "database.db"

# class User:
#     def __init__(self, id, username, password):
#         self.id = id
#         self.username = username
#         self.password = password
#
# users = []
# users.append(User(id=1, username='Username', password='Password'))
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))

def create_database(app):
    if not path.exists('weather/' + DB_NAME):
        db.create_all(app=app)


app = Flask(__name__, template_folder="templates")
app.secret_key = 'iswearifanotheroceanidsummonsawaterbirdiwillripitslungsout'
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
db.init_app(app)



from minilabs.adam import adam_bp
#from User import User
#from minilabs.ethan import ethan_bp WIP
from minilabs.ethansecond import ethan2_bp
from minilabs.kaila import kaila_bp
from minilabs.nolan import nolan_bp
from minilabs.sophie import sophie_bp


app.register_blueprint(adam_bp, url_prefix='/adam')
#app.register_blueprint(User, url_prefix='/user')
#app.register_blueprint(ethan_bp, url_prefix='/ethan') WIP
app.register_blueprint(ethan2_bp, url_prefix='/ethan2')
app.register_blueprint(kaila_bp, url_prefix='/kaila')
app.register_blueprint(nolan_bp, url_prefix='/nolan')
app.register_blueprint(sophie_bp, url_prefix='/sophie')

create_database(app)



## home page ##
@app.route("/")
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.pop('user_id', None)
        session.permanent = True
        username = request.form['username']
        password = request.form['password']
        # try:
        #     user = [x for x in users if x.username == username][0]
        #     if user and user.password == password:
        #         session['user_id'] = user.id
        #         return render_template('weather.html')
        #     else:
        #         return render_template('login.html')
        # except:
        #     return redirect(url_for('login'))
    else:
        if 'user' in session:
            return redirect(url_for('weather'))
    return render_template('login.html', insession = False)

@app.route('/signup', methods=["POST", "GET"])
def signup():

    if request.method == "POST":
        username = request.form['username2']
        password = request.form['password2']

        user = User.query.filter_by(username=username).first()
        if user:
            flash('Username Already Exists!')
            return render_template("login.html")
        else:
            new_user = User(username=username, password=password)
            db.session.add(new_user)
            db.session.commit()
            flash('Account Created!')
    return render_template("home.html")

@app.route('/weather')
def weather():
    return render_template('weather.html')

@app.route('/minilabs')
def minilabs():
    return render_template('minilabs.html')

if __name__ == "__main__":
    app.run(host='localhost', port=25565)

#when pushing, keep app.run(host='127.0.0.1', port=5000)
#school app.run(host='10.8.137.78', port=25565)
#nolan's app.run(host='192.168.1.14', port=25565)
#zerotierone app.run(host='192.168.193.211', port=25565)