class Foods:
    def classFunction(self):
        print("Hello, my name is " + self.name + ", I am " + self.age + " years old. My favorite foods are " + self.food1 + ", " + self.food2 + ", and " + self.food3 + "!")

self = Foods()
self.name = "Adam"
self.age = "18"
self.food1 = "pizza"
self.food2 = "tacos"
self.food3 = "burgers"

self.classFunction()