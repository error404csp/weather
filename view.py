from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)
app.config['ENV'] = 'development'
app.config['DEBUG'] = True

## home page ##
@app.route("/")
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/weather')
def recipes():
    return render_template('weather.html')

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
