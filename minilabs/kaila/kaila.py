from flask import Flask, render_template, request
from minilabs.kaila import kaila_bp

class introduction:
    def classFunction(self):
        return "Hi my name is " + self.name + ", I am currently " + self.age + ", and I like " + self.hobby1 + ", " + self.hobby2 + ", and playing " + self.hobby3

# my class
r1 = introduction()
r1.name = "Kaila"
r1.age = "17"
r1.hobby1 = "singing"
r1.hobby2 = "drawing"
r1.hobby3 = "games"

r1.classFunction()

app = Flask(__name__)

@kaila_bp.route('/kailaData')
def minilabkaila():
        return render_template("kaila.html")

@kaila_bp.route('/kailaDataTwo', methods=["POST"])
def minilabkailaTwo():
    if request.method == "POST":
        return render_template("kaila.html", kailasData=r1.classFunction())
