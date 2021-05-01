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

sortedlist = bubblesort([2, 4, 6, 5, 3, 2, 7, 6, 9, 22, 6])

print(sortedlist)

app = Flask(__name__)

@sophie_bp.route('/bubble', methods=["GET", "POST"])
def bubblesort():
    if request.method == 'POST':
        first = int(request.form['first'])
        second = int(request.form['second'])
        third = int(request.form['third'])
        fourth = int(request.form['fourth'])
        fifth = int(request.form['fifth'])
        numberlist = [first, second, third, fourth, fifth]
        list = [first, second, third, fourth, fifth]
        sortedlist = bubblesort(numberlist)
        return render_template("sophie.html", first=first, second=second, third=third, fourth=fourth, fifth=fifth,  list=list, sortedlist=sortedlist, numberlist=numberlist)
    return render_template("sophie.html")
