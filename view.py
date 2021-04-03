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
def weather():
    return render_template('weather.html')

@minilabs.route('/kaila')
def kaila():
    return render_template("/minilabs/kaila.html")

@minilabs.route('/adam')
def adam():
    return render_template("/minilabs/adam.html")

@minilabs.route('/nolan')
def nolan():
    return render_template("/minilabs/nolan.html")

@minilabs.route('/ethan')
def ethan():
    return render_template("/minilabs/ethan.html")

@minilabs.route('/sophie')
def sophie():
    return render_template("/minilabs/sophie.html")

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
