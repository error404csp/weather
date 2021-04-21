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

def selectionSort(string,dumb):
    #split list by comma into integers, characters, or strings
    listedData = string.replace(" ",",")
    listedData = listedData.split(",")
    listedData = [i for i in listedData if i != "," and i != ""]

    #bubble sort
    def sortVal(values):
        for i in range(len(values)):
            min_i = i
            for j in range(i+1, len(values)):
                if values[min_i] > values[j]:
                    min_i = j
            values[i], values[min_i] = values[min_i], values[i]
        return values

    #assume list is integers, try sorting integers
    try:
        #turn strings of integers into integers
        listedData = [int(n) for n in listedData]
        #sort integers
        listedData = sortVal(listedData)
        stringList = ", ".join([str(i) for i in listedData])
        return stringList

    #if this fails, the list is characters/strings
    except:
        #rule out mix of data types
        for i in listedData:
            try:
                if int(i):
                    raise TypeError
            except ValueError:
                pass

        #sort characters
        if all(len(s) == 1 for s in listedData):
            sortedCharacters = sortVal(listedData)
            stringList = ", ".join(sortedCharacters)
            return stringList

        #sort words into alphabetical order
        listedData = sortVal(listedData)

        #sort each word into alphabetical order (depends on checkbox)
        if dumb == "true":
            for i in range(len(listedData)):
                sortedWord = "".join(sortVal(list(listedData[i])))
                listedData[i] += ": " + sortedWord

        #creates stringList of the listed words
        stringList = ", ".join(listedData)

        #no early return --> returns words
        return stringList

app = Flask(__name__)

@nolan_bp.route('/minilab')
def minilab():
    return render_template("nolan.html")

@nolan_bp.route('/fibGetter', methods=["POST"])
def fibGetter():
    if request.method == "POST":
        try:
            initial = int(request.form["initial"])
            goBack = int(request.form["goBack"])
            nPass = int(request.form["nPass"])
            gotem = fibAndMore(initial,goBack,nPass)
            return jsonify({'statement':gotem.fibState(), 'sequence': gotem.fibFinity()})
        except:
            return jsonify({'error':'Enter integers in a digit form (1, 3, 4, etc).'})

@nolan_bp.route('/bubbleSort', methods=['POST'])
def bubbleSort():
    if request.method == "POST":
        try:
            dataToSort = request.form["dataToSort"].lower()
            checked = request.form.get("chuckeecheese")
            sortedList = selectionSort(dataToSort,checked)
            return jsonify({'sortedData':sortedList})
        except:
            return jsonify({'error':"Make sure the data is all the same type and doesn't have any weird characters fucking it up."})