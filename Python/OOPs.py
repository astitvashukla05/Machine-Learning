# Modelling a bank accocunt

class Account:
    def __init__(self,number,balance=0):
        self.number=number
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        return "Money deposited successfully"
    def withdraw(self,amount):
        if(self.balance<amount):
            return "money cannot be withdrawn"
            
        else:
            self.balance-=amount
            return "Money gone"

acc1=Account(1234,1000)
print(acc1.number)
print(acc1.balance)
print(acc1.withdraw(500))
print(acc1.deposit(100))
print(acc1.balance)

print(acc1.withdraw(50000))

# INHERITANCE

class Car:
    def __init__(self,engine,door,window):
        self.windows=window
        self.doors=door
        self.engine=engine
    def drive(self):
            print("The person is driving "+self.engine)

class Tesla(Car):
    def __init__(self,windows,door,engine,isSelfDriving):
        super().__init__(engine,door,windows)
        self.isSelfDriving=isSelfDriving
    def selfDrive(self):
        print(f"Tesla is self driving: {self.isSelfDriving}")

tesla1=Tesla(4,2,"123cc",True)
print(tesla1.windows)
print(tesla1.doors)
print(tesla1.engine)
tesla1.selfDrive()
(tesla1.drive())
print(tesla1)
class Animal:
    def __init__(self,species,kind):
        self.species=species
        self.kind=kind
    def desc(self):
        print(f"This animal is of species {self.species} and he is of {self.kind} kind")

class Mammal:
    def __init__(self,birth):
        self.birth=birth
    def reproduce(self):
        print(f"This {self.kind} reproduces through {self.birth}")

class Human(Animal,Mammal):
    def __init__(self,species,kind,birth):
        Animal.__init__(self,species,kind)
        Mammal.__init__(self,birth)
        
h1=Human("Homo","Man","Sexual")
(h1.kind)
(h1.species)
(h1.birth)
h1.reproduce()
class H1:
    def speak(self):
        print("says hello")

class H2(H1):
    def speak(self):
        print("says hi")
        
class H3(H1):
    def speak(self):
        print("says you")
        
h2=H2()
h1=H1()
h3=H3()
h1.speak()
h2.speak()
h3.speak()

class Shapes():
    def area():
        print("Area of shapes we give")

class Circle(Shapes):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        print("Area of the circle is ",3.14*self.radius*self.radius)
class Square(Shapes):
    def __init__(self,side):
        self.side=side
    def area(self):
        print("Area of sq is ",self.side*self.side)
        
sq=Square(5)
sq.area()
ci=Circle(3)
ci.area()

class Person:
    def __init__(self,name,age):
        self.name=name
        self.__age=age
    def getAge(self):
        print(self.__age)
        
p1=Person("astitva",12)
print(dir(p1))
#print(p1.__name)
(p1.getAge())

lit=[1,2,3,4,5]
iterat=iter(lit)

try:
    next(iterat)
except StopIteration:
    print("An error")
