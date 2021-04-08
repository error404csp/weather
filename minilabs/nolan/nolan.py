from flask import Flask, render_template, request, jsonify
from minilabs.nolan import nolan_bp

class fibAndMore:
    def __init__(self,initial,goBack, nPass):
        self.initial = initial
        self.goBack = goBack
        self.nPass = nPass
    def fibState(self):
        return f"Starting with {self.initial}, going back {self.goBack} numbers from each consecutive number, the first {self.nPass} numbers in the sequence would go like this:"
    def fibFinity(self):
        fibSet = [self.initial]
        for i in range(0,self.goBack):
            fibSet.insert(0,0)
        fibString = ""
        for i in range(self.goBack,self.nPass+self.goBack-1):
            fibAppendment = fibSet[i]
            for j in range(1, self.goBack):
                fibAppendment += fibSet[i - j]
            fibSet.append(fibAppendment)
        for i in range(self.goBack,len(fibSet)):
            fibString += " " + str(fibSet[i])
        return fibString

app = Flask(__name__)

@nolan_bp.route('/minilab')
def minilab():
    return render_template("nolan.html")

@nolan_bp.route('/minilabFunc', methods=["POST"])
def minilabFunc():
    if request.method == "POST":
        try:
            initial = int(request.form["initial"])
            goBack = int(request.form["goBack"])
            nPass = int(request.form["nPass"])
            gotem = fibAndMore(initial,goBack,nPass)
            return jsonify({'statement':gotem.fibState(), 'sequence': gotem.fibFinity()})
        except:
            return jsonify({'error':'Enter integers in a digit form (1, 3, 4, etc).'})