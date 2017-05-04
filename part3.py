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
