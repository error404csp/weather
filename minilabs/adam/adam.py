from minilabs.adam import adam_bp
from flask import Flask, render_template, request, jsonify

import random

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


