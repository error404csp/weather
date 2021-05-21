from flask import Blueprint, render_template, request

User = Blueprint('User', __name__)

@User.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == "POST":
        x = 1
    return render_template("login.html", boolean=True)