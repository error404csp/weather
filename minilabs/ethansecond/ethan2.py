from flask import Flask, render_template, request
from minilabs.ethansecond import ethan2_bp

class ethanbubble:
    def __init__(self):
        self.jesus = []
    def bubble(self):
        list = self.jesus
        for i in range(len(list) - 1):
            for j in range(len(list) - 1):
                if int(str(list[j])) > int(str(list[j+1])):
                    print("switch:")
                    print(list[j])
                    print(list[j+1])

                    k = list[j+1] #switches [j] and [j+1]
                    list[j+1] = list[j]
                    list[j] = k

                    print(list)
            print("-----")
        return list



app = Flask(__name__)

@ethan2_bp.route('/ethan2Bubble')
def minilabethan2():
    return render_template("ethan2.html")

@ethan2_bp.route('/ethan2BubbleTwo', methods=["POST"])
def minilabethan2Two():
    if request.method == "POST":
        r1 = ethanbubble()
        big = request.form["numbers"]
        big2 = big.split()
        big3 = []
        for i in big2:
            big3.append(i)
            print(i)
        r1.jesus = big3
        print(big3)
        return render_template("ethan2.html", ethan2Data=r1.bubble())