from minilabs.adam import adam_bp
from flask import Flask, render_template, request, jsonify, Blueprint

import random
import logging


factlist = ["Fungi known as Ophiocordyceps, infects ants' central nervous system and turns them into zombie-like creatures","Armadillo shells are bulletproof","The longest english word is 189,819 letters long","The Eiffel Tower can grow 6+ inches during the summer due to the heat"]

class Facts:
    def __init__(self, series):
        if series < 0 or series > 5:
            raise ValueError("Series must be between 0 and 5")
        self._series = series
        self._list = []
        self._dict = {}
        self._dictID = 0
        self.fact_series()

    def fact_series(self):
        limit = self._series
        f = [random.sample((factlist), k=2)]
        while limit > 0:
            self.set_data(f[0])
            f = [f[0]]
            limit = limit - 1

    def set_data(self, num):
        self._list.append(num)
        self._dict[self._dictID] = self._list.copy()
        self._dictID += 1

    @property
    def series(self):
        return self._series

    @property
    def list(self):
        return self._list

    @property
    def number(self):
        return self._list[self._dictID - 1]

    def get_sequence(self, nth):
        return self._dict[nth]

@adam_bp.route('/minilab', methods=['GET','POST'])
def minilabadam():
    if request.method == "POST":
        a = int(request.form["series"])
        randomfact = Facts(a)
        randomfact.fact_series()
        return render_template("adam.html", data=randomfact.get_sequence(a))
    return render_template("adam.html", data="")





def bubblesort(Nothing, i):
    if int(Nothing[i])>int(Nothing[i+1]):
        value=Nothing[i]
        Nothing[i]=Nothing[i+1]
        Nothing[i+1]=value




@adam_bp.route('/BubbleSort', methods=['GET','POST'])
def something():
    if request.method == "POST":
        a = (request.form["numbers"])
        # results = sort(a)
        sortnumber=a
        #logging.log(sortnumber)
        numbers = sortnumber.split(' ')
        for j in range (0,len(numbers)-1):
            for i in range (0, len(numbers)-1):
                bubblesort(numbers, i)
        return render_template("adam.html", databubblesort=numbers)
    return render_template("adam.html", databubblesort="")





