class Person:
    def __init__(self,name,age,birthday,likes):
        self.name = name
        self.age = age
        self.birthday = birthday
        self.likes = likes
    def showData(self):
        return f"Hi, I'm {self.name}. I am {self.age} years old, and I was born on {self.birthday}. I like {self.likes}."
    def ageFibonnaci(self, n):
        fibSet = [0, self.age]
        fibString = ""
        for i in range(1,n):
            fibSet.append(fibSet[i] + fibSet[i-1])
            fibString += " " + str(fibSet[i])
        return f"If you were to create a fibonnaci sequence starting with my age, the first {n} numbers would go like this:" + fibString
Nolan = Person("Nolan D'Esopo", 18, "October 17, 2002", "playing guitar, riding my bike, listening to music, and playing video games")
nPass = int(input("How many fibonnaci numbers do you want?"))

print(Nolan.showData())
print(Nolan.ageFibonnaci(nPass))