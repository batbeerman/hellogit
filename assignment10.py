#Q1Create a class Animal
class animal:
    def animalattribute(self):
        print("This is the method of base class")
class tiger(animal):
    def tiger(self):
        print("This is the method of inherited class")
t=tiger()
t.animalattribute()



#Q2
#Output
#A B
#A B



#Q3 Create a class Cop
class Cop:
   def __init__(self, name, age, work, exp, des):
        self.name = name
        self.age = age
        self.work = work
        self.exp = exp
        self.des = des

   def add(self, name, age, work, exp, des):
       self.name = name
       self.age = age
       self.work = work
       self.exp = exp
       self.des = des

   def display(self):
       print(self.name, self.age, self.work, self.exp, self.des, sep = '\n')

   def update(self, name, age, work, exp, des):
       self.name = name
       self.age = age
       self.work = work
       self.exp = exp
       self.des = des

class Mission(Cop):
       def add_mission_details(self):
        print('Available for mission')

m = Mission('Saurav', 23, 'agent', 2, 'Lt.\n')
m.display()
m.add('Praveen', 26, 'Special_Forces', 9, 'Major\n')
m.display()
m.update('Gaurav', 25, 'Armoured', 4, 'Cap\n')
m.display()
m.add_mission_details()



#Q4 Create a class Shape
class shape:
    def __init__(self, length, breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        area=self.length*self.breadth
        print("Area is:", area)
class rectangle(shape):
    def __init__(self, length, breadth):
        self.length=length
        self.breadth=breadth
class square(shape):
    def __init__(self, length, breadth):
        self.length=length
        self.breadth=breadth
r=rectangle(56,76)
r.area()
s=square(56,56)
s.area()
