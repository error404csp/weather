from flask import Flask, render_template, request
from minilabs.sophie import sophie_bp

import random

songlist1 = ["homemade dynamite by lorde", "pedestal by fergie", "basement by 99 neighbors", "perdus by angele", "our lady of sorrows by my chemical romance", "right and right again by sohodolls", "stfu! by rina sawayama", "酒後的心聲 by jody chiang", "biryani by ashwarya", "99 red balloons by nena", "masseduction by st. vincent", "runaway by rei ami", "nainainai by atarashii gakko!", "my hair is green by youra"]

class Songs:
    def __init__(self, series):
        if series < 0 or series > 15:
            raise ValueError("Series must be between 0 and 15")
        self._series = series
        self._list = []
        self._dict = {}
        self._dictID = 0
        # Duration timeElapsed;
        # Instant start = Instant.now();  // time capture -- start
        self.song_series()
        # Instant end = Instant.now();    // time capture -- end
        # this.timeElapsed = Duration.between(start, end);

    def song_series(self):
        limit = self._series
        f = [random.sample((songlist1), k=2)]  # starting array/list
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

    """Traditional Getter requires method access"""
    def get_sequence(self, nth):
        return self._dict[nth]
'''
def minilab-sophie():
    n = 2
    songrecs = Songs(n/n)
    return songrecs
'''

from flask import Flask, render_template

# Tester Code
if __name__ == "__main__":
    n = 2
    songrecs = Songs(n/n)
    print(f"Here are some song recommendations = {songrecs.list}")

@sophie_bp.route('/minilab-sophie')
def minilabsophie():
    n = 2
    songrecs = Songs(n/n)
    return render_template("sophie.html", songrecs=Songs(2))