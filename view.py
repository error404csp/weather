from flask import Blueprint, Flask, redirect, url_for, render_template, request, session, flash
from flask_sqlalchemy import SQLAlchemy
import requests, json
from flask_login import UserMixin, login_user, LoginManager

app = Flask(__name__, template_folder="templates")
app.config['SESSION_TYPE'] = 'filesystem'
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True
app.secret_key = 'super secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

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

db = SQLAlchemy(app)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

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
        username = request.form.get("username1")
        password = request.form.get("password1")
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
    username = request.form.get("username2")
    password = request.form.get("password2")
    user = User.query.filter_by(username=username).first()
    if user:
        flash('Username Already Exists!', category='error')
    else:
        new_user = User(username=username,password=password)
        db.session.add(new_user)
        db.session.commit()
        flash('Account Created!', category='success')
    return render_template("login.html")

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route('/weather')
def weather():
    return render_template('weather.html')

@app.route('/minilabs')
def minilabs():
    return render_template('minilabs.html')

#weather API
@app.route('/weatherAPI', methods=['POST'])
def weatherAPI():
    weatherAPI = "api.openweathermap.org/data/2.5/forecast"
    cityId = request.get_json()
    apiKey = "6eb40bfe1bcc41e01f9b695559dcd244"
    link = "http://" + weatherAPI + "?id=" + cityId + "&appid=" + apiKey
    weatherData = requests.get(link)
    #print(weatherData.text)
    return weatherData.text

if __name__ == "__main__":
    app.run(host='localhost', port=25565)

#when pushing, keep app.run(host='127.0.0.1', port=5000)
#nolan's app.run(host='192.168.1.14', port=25565)