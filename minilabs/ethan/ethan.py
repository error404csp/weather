from flask import Flask, render_template, request
from minilabs.ethan import ethan_bp

class math:

    def derivative(self):
        s = self.slope
        e = self.exponent
        x = self.x
        ans = (s*e)(x^(e-1))
        return ans

    def integral(self):
        s = self.slope
        e = self.exponent
        a = self.a
        b = self.b
        ans = s(1/(e+1))(a^(e+1)) - s(1/(e+1))(b^(e+1))
        return ans

# my class
numbers = math()
numbers.slope = 5
numbers.exponent = 5
numbers.x = 5
numbers.a = 5
numbers.b = 10

numbers.integral()
numbers.derivative()

app = Flask(__name__)

@ethan_bp.route('/ethan-minilab')
def minilabethan():
    return render_template("ethan.html", integral=numbers.integral(), derivative=numbers.derivative())
