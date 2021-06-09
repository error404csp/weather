from flask import Flask, redirect, url_for, render_template, request, session, flash
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import UserMixin, login_user, LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"

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

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if user:
            if user.password == password:
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return render_template("login.html")
            else:
                flash('Incorrect Password', category='error')
        else:
            flash('Username does not exist.', category='error')
    return render_template("login.html")

@app.route('/signup', methods=["POST", "GET"])
def signup():

    if request.method == "POST":
        username = request.form['username2']
        password = request.form['password2']

        user = User.query.filter_by(username=username).first()
        if user:
            flash('Username Already Exists!', category='error')
            return render_template("login.html")
        else:
            new_user = User(username=username, password=password)
            db.session.add(new_user)
            db.session.commit()
            flash('Account Created!', category='success')
    return render_template("login.html")


@app.route('/weather')
def weather():
    return render_template('weather.html')

@app.route('/minilabs')
def minilabs():
    return render_template('minilabs.html')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

if __name__ == "__main__":
    app.run(host='localhost', port=25565)