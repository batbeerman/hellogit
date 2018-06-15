#Q1
class circle:
    def __init__(self, radius):
        self.r = radius

    def GetArea(self):
        area = 3.14 * (self.r) * (self.r)
        print("The area is", area)

    def GetCircum(self):
        circum = 2 * (3.14) * self.r
        print("The radius is", circum)


x = circle(3.5)
x.GetCircum()
x.GetArea()




#Q2
class Student:
    def __init__(self, name, ron):
        self.nam = name
        self.ro = ron

    def print(self):
        print("Name:", self.nam)
        print("Roll no:", self.ro)


x = Student("Praveen", 35)
x.print()



#Q3
class temperature:
    def convertf():
        t = int(input("Enter termperature in celsius"))
        temp = (1.8 * t) + 32
        print("Temperature in fahrenheit is", temp)

    def convertc():
        t = int(input("Enter termperature in fahrenheit"))
        temp = (t - 32) * 0.5556
        print("Temperature in celsius is", temp)


x = temperature
x.convertf()
x.convertc()



#Q4
class Movie:
    def __init__(self, mname, aname, year, ratings):
        self.mn = mname
        self.an = aname
        self.y = year
        self.rating = ratings

    def updatedetails(self):
        self.mn = input("Enter movie name:")
        self.an = input("Enter the artist's name:")
        self.y = input("Enter the year:")
        self.rating = input("Enter rating out of five:")

    def output(self):
        print("The movie's name is:", self.mn)
        print("The artist's name is:", self.an)
        print("The year is:", self.y)
        print("The year is:", self.rating)


x = Movie("Ram teri ganga maili", "Nana patekar", 1978, 4.5)
x.output()
x.updatedetails()
x.output()




#Q5
class Expendi:
    def __int__(self, expend, savings):
        self.ex = expend
        self.sa = savings

    def print1(self):
        print("Expenditure is", self.ex)
        print("Savings are:", self.sa)

    def calc(self):
        self.salary = self.sa + self.ex

    def display(self):
        print("The total salary is:", self.salary)


x = Expendi(266,7600)
x.print1()
x.calc()
x.display()
