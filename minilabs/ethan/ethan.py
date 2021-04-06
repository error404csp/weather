class math:
    def integral(numbers):
        a = (numbers.slope*numbers.b) - (numbers.slope*numbers.a)
        print("Integral:" + a)
    def derivative(numbers):
        print("Derivative:" + numbers.slope*0)

# my class
numbers = math()
numbers.slope = 3
numbers.a = 3
numbers.b = 10

numbers.integral()
numbers.derivative()

if __name__ == "__main__":
    a = 1
