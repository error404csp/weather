from flask import Flask, render_template, request
from minilabs.sophie import sophie_bp

def bubblesort(list):
    num_length = len(list) - 1
    sorted = False

    while not sorted:
        sorted = True
        for a in range(0, num_length):
            if list[a] > list[a + 1]:
                sorted = False
                list[a], list[a + 1] = list[a + 1], list[a]

    return list

app = Flask(__name__)

@sophie_bp.route('/bubble', methods=["GET", "POST"])
def bubblesortProc():
    if request.method == 'POST':
        first = int(request.form['first'])
        second = int(request.form['second'])
        third = int(request.form['third'])
        fourth = int(request.form['fourth'])
        fifth = int(request.form['fifth'])
        sortedList = bubblesort([first, second, third, fourth, fifth])
        return render_template("bubble.html", sortedlist=sortedList, numberlist=[first, second, third, fourth, fifth])
    return render_template("bubble.html")
