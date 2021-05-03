from flask import Flask, redirect, url_for, render_template

app = Flask(__name__, template_folder="templates")
app.config['ENV'] = 'development'
app.config['DEBUG'] = True

from minilabs.adam import adam_bp
#from minilabs.ethan import ethan_bp WIP
from minilabs.ethansecond import ethan2_bp
from minilabs.kaila import kaila_bp
from minilabs.nolan import nolan_bp
from minilabs.sophie import sophie_bp
app.register_blueprint(adam_bp, url_prefix='/adam')
#app.register_blueprint(ethan_bp, url_prefix='/ethan') WIP
app.register_blueprint(ethan2_bp, url_prefix='/ethan2')
app.register_blueprint(kaila_bp, url_prefix='/kaila')
app.register_blueprint(nolan_bp, url_prefix='/nolan')
app.register_blueprint(sophie_bp, url_prefix='/sophie')

## home page ##
@app.route("/")
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/weather')
def weather():
    return render_template('weather.html')

@app.route('/minilabs')
def minilabs():
    return render_template('minilabs.html')

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)

#when pushing, keep app.run(host='127.0.0.1', port=5000)
#nolan's app.run(host='192.168.1.88', port=25565)
