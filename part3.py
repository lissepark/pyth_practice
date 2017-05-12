'''2.3 Напишіть два скрипта представлених вище. Подивіться, як вони працюють. У другу програму додайте
ще одну властивість і один метод, що дозволяє її міняти. Створіть третій об'єкт і змініть всі його властивості.
Напишіть програму в стилі ООП, що задовольняє наступним умовам: в програмі повинні бути два класи і два
об'єкти, що належать різним класам; один об'єкт за допомогою методу свого класу повинен так чи інакше обробляти
дані іншого об'єкта: obj1.МЕТОД (obj2.СВОЙСТВО).'''
class First:
    color = 'red'

    def changecolor(self,newcolor):
        self.color = newcolor

class Second:
    color = 'red'
    form = 'circle'
    #one more property
    name = 'wheel'

    def changecolor(self,newcolor):
        self.color = newcolor

    def changeform(self,newform):
        self.form = newform
    #one more method
    def changeName(self,newname):
        self.name = newname

obj1 = Second()
obj2 = Second()
obj3 = Second()

print(obj1.color, obj1.form)
print(obj2.color, obj2.form)
print(obj3.color, obj3.form, obj3.name)

obj1.changecolor('blue')
obj2.changecolor('green')
obj2.changeform('triangle')

obj3.changecolor('orange')
obj3.changeform('polygon')
obj3.changeName('not whell')

print(obj1.color, obj1.form)
print(obj2.color, obj2.form)
print(obj3.color, obj3.form, obj3.name)


class Res:
    value = 0

    def changeValue(self,newValue):
        self.value = newValue

class Propert:
    resSum = 0

    def finRes(self,num):
        self.resSum = 5+num

obj11 = Res()
obj11.changeValue(7)

obj12 = Propert()
obj12.finRes(obj11.value)
print(obj12.resSum)


class YesInit:
    def __init__(self,one = "noname",two = "nonametoo"):
        self.fname = one
        self.sname = two

obj1 = YesInit("Sasha","Second")
obj2 = YesInit()
obj3 = YesInit('Spartak')
obj4 = YesInit(two='Harry')

print(obj1.fname,obj1.sname)
print(obj2.fname,obj2.sname)
print(obj3.fname,obj3.sname)
print(obj4.fname,obj4.sname)
'''output:
Sasha Second
noname nonametoo
Spartak nonametoo
noname Harry'''

class Building:
     def __init__(self,w,c,n=0):
          self.what = w
          self.color = c
          self.numbers = n
          self.mwhere(n)
 
     def mwhere(self,n):
          if n <= 0:
               self.where = "отсутствуют"
          elif 0 < n < 100:
               self.where = "малый склад"
          else:
               self.where = "основной склад"
 
     def plus(self,p):
          self.numbers = self.numbers + p
          self.mwhere(self.numbers)
     def minus(self,m):
          self.numbers = self.numbers - m
          self.mwhere(self.numbers)
 
m1 = Building("доски", "белые",50)
m2 = Building("доски", "коричневые", 300)
m3 = Building("кирпичи","белые")
 
print (m1.what,m1.color,m1.where)
print (m2.what,m2.color,m2.where)
print (m3.what,m3.color,m3.where)
 
m1.plus(500)
print (m1.numbers, m1.where)
'''доски белые малый склад
доски коричневые основной склад
кирпичи белые отсутствуют
550 основной склад'''
'''В який момент створюється атрибут where об'єктів?
При створенні (ініціалізації) об"єкта.
Навіщо знадобилося конструкцію if-elif-else винести в окрему функцію, а не залишити її в методі __init__?
Метод __init__ виконується раз при створенні (ініціалізації) об"єкта,
а конструкція if-elif-else потрібна кожного разу при виклику методу mwhere(self,n)  
Самостійно придумайте клас, що містить конструктор. Створіть на його основі кілька об'єктів.'''
class Book:
    def __init__(self,title,author,year):
          self.title = title
          self.author = author
          self.year = year

    def changeTitle(self,title):
          self.title = title
    def changeAuthor(self,author):
          self.author = author
    def changeYear(self,year):
          self.year = year
 
b1 = Book('B&G','Man1','1990')
b2 = Book('R&Y','Man2','1975')
print(b1.title,b1.author,b1.year)
print(b2.title,b2.author,b2.year)
b1.changeTitle('B&G2')
b1.changeYear('1989')
print(b1.title,b1.author,b1.year)
'''B&G Man1 1990
R&Y Man2 1975
B&G2 Man1 1989'''


class Table:
     def __init__(self,l,w,h):
          self.long = l
          self.width = w
          self.height = h
     def outing(self):
          print (self.long,self.width,self.height)


class Kitchen(Table):
     def howplaces(self,n):
          if n < 2:
               print ("It is not kitchen table")
          else:
               self.places = n
     def outplases(self):
          print (self.places)


t_room1 = Kitchen(2,1,0.5)
t_room1.outing()
t_room1.howplaces(5)
t_room1.outplases()
 
t_2 = Table(1,3,0.7)
t_2.outing()
#t_2.howplaces(8) # ОШИБКА

#once more class
class OfficeTable(Table):
     def setForm(self,form):
          self.form = form
     def setColor(self,color):
          self.color = color

officeTable = OfficeTable(2,3,1)
officeTable.outing()
officeTable.setForm('oval')
officeTable.setColor('brown')
print(officeTable.color,officeTable.form)

'''2.8 Напишіть програму, де клас «геометричні фігури» (figure) містить властивість color з початковим
значенням white і метод для зміни кольору фігури, а його підкласи «овал» (oval) і «квадрат» (square) містять методи
__init__ для завдання початкових розмірів об'єктів при їх створенні.'''
class Figure:
     color = 'white'
     def colorChange(self,newColor):
          self.color = newColor

class Oval(Figure):
     def __init__(self,length=100,width=60):
          self.length = length
          self.width = width
     def setLength(self,newLength):
          self.length = newLength
     def setWidth(self,newWidth):
          self.width = newWidth

class Square(Figure):
     def __init__(self,side=60):
          self.side = side
     def setSide(self,newSide):
          self.side = newSide

oval = Oval()
square = Square()

print(oval.color,oval.length,oval.width)
print(square.color,square.side)

oval.colorChange('green')
oval.setLength(80)
square.colorChange('blue')
square.setSide(75)
print(oval.color,oval.length,oval.width)
print(square.color,square.side)

'''Напишіть програму, що запитує у користувача введення числа. Якщо число належить діапазону від -100 до
100, то створюється об'єкт одного класу, в усіх інших випадках створюється об'єкт іншого класу. В обох класах
повинен бути метод-конструктор __init__, який в першому класі зводить число в квадрат, а по-другому – множить на
два.'''
class Sqr:
    def __init__(self,n):
        self.res = n*n
        print(self.res)

class Mult:
    def __init__(self,n):
        self.res = n*2
        print(self.res)

inp = input('Please type a number')
n = int(inp)
if n < 100 and n > (-100):
    sqrr = Sqr(n)
else:
    mult = Mult(n)

'''Напишіть невелику об'єктно-орієнтовану програму, яка демонструвала б такі властивості ООП як спадкування
і поліморфізм.'''
class Vehicle:
     def __init__(self,wheel=4,door=2,steering='right'):
          self.wheel = wheel
          self.door = door
          self.steering = steering

     def out(self):
          print(self.wheel,self.door,self.steering)

class Track(Vehicle):
     wheel = 10          
     def out(self):
          print("It's a track")
          Vehicle.out(self)
          print('track go')

class Van(Vehicle):
     door = 5
     def out(self):
         print("It's a van")
         Vehicle.out(self)
         print('van go')

vehicle = Vehicle()
vehicle.out()
print('-----------------------------------------')
track = Track()
track.wheel = 10
track.out()
print('-----------------------------------------')
van = Van()
van.door = 5
van.out()


class Win_Door:
     def __init__(self,x,y):
          self.square = x * y

class Room:
     def __init__(self,x,y,z):
          self.square = 2 * z * (x + y)
     def win_door(self, d,e, f,g, m=1,n=1):
          self.window = Win_Door(d,e)
          self.door = Win_Door(f,g)
          self.numb_w = m
          self.numb_d = n
     def wallpapers(self):
          self.wallpapers = self.square - \
               self.window.square * self.numb_w \
               - self.door.square * self.numb_d
     def printer(self):
          print ("Площадь стен комнаты равна "\
          ,str(self.square)," кв.м")
          print ("Оклеиваемая площадь равна: ", \
               str(self.wallpapers), " кв.м")

labor34 = Room(5,4,2)
labor34.win_door(1.5,1.5, 2,1, 2)
labor34.wallpapers()
labor34.printer()
'''Площадь стен комнаты равна  36  кв.м
Оклеиваемая площадь равна:  29.5  кв.м'''

'''Спробуйте самостійно придумати задачу, для вирішення якої можна використовувати композиційний підхід.
Напишіть програму на Python.'''
class Engine:
     def __init__(self,m=100):
          self.m = m
          print('Engine\'s weight is: ',m,'kg')
          
class CarBody:
     def __init__(self,m=100):
          self.m = m
          print('Car body\'s weight is: ',m,'kg')
     
class Car:
     def __init__(self,m=600):
          self.m = m
     def mEngine(self,mE):
          self.mE = Engine(mE)
     def mCarBody(self,mCB):
          self.mCB = CarBody(mCB)
     def calcWeight(self):
          self.totalWeight = self.m+self.mE.m+self.mCB.m
          print('Car\'s total weight is: ',self.totalWeight,'kg')

car1 = Car()
car1.mEngine(150)
car1.mCarBody(140)
car1.calcWeight()

'''Доповніть клас методами __mul__ (викликається при використанні об'єкта в операціях множення) і __sub__ (віднімання).
Викличте дані методи за допомогою відповідних операцій з об'єктами.'''
class Newclass:
     def __init__(self,base):
          self.base = base
     def __add__(self,a):
          self.base = self.base+a
     def __mul__(self,a):
          self.base = self.base*a
     def __sub__(self,a):
          self.base = self.base-a
     def __str__(self):
          return "%s !!! " % self.base

a = Newclass(10)
a + 20
print(a)
a - 10
print(a)
a*5
print(a)
print("------------------------------------------------------")

b = Newclass("yes")
b+"terday"
print(b)
b*5
print(b)
#b - "ay" ERROR
print("------------------------------------------------------")

c = Newclass([2,6,3])
c+[7,1]
print(c)
c * 5
print(c)
#c - 3 ERROR

'''Для яких об'єктів неможливо використовувати метод __sub__?
для строк та списків'''








