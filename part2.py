'''Exercise 1.6.1. Write a program underscores.py that would input a phrase from the user and
print out the phrase with the white space between words replaced by an underscore. For instance if the input
is "the best one", then it would print "the_best_one". The conversion can be done in one or two statements
using the recent string methods.'''
a = input("Enter text, please: ")
aseq = a.split(' ')
aseq2 = '_'.join(aseq)
aseq2

'''Exercise 1.6.2. An acronym is a string of capital letters formed by taking the first letters from
a phrase. For example, SADD is an acronym for ’students against drunk driving’. Note that the acronym
should be composed of all capital letters even if the original words are not. Write a program acronym.py
that has the user input a phrase and then prints the corresponding acronym.'''
a = input("Enter text, please: ")
aseq = a.split(' ')
l = len(aseq)
yt = ""
for i in range(l):
    print(aseq[i][0].upper())
    yt = yt + aseq[i][0].upper()
yt

'''Exercise 3.3.1 . Rename the example file locationsStub.py to be locations.py, and complete the
function printLocations, to print the index of each location in the string s where target is located. For example,
printLocations(’This is a dish’, ’is’) would go through the string ’This is a dish’ looking
for the index of places where ’is’ appears, and would return [2, 5, 11]. Similarly printLocations(’This
is a dish’, ’h’) would return [1, 13]. The program stub already uses the string method count. You
will need to add code using the more general form of find.'''
def printLocations(whereFind, whatFind):
    start = 0
    end = 0
    c = whereFind.count(whatFind)
    lst = list()
    print(len(whatFind))
    for i in range(c):
        start = whereFind.find(whatFind, end)
        end = start + len(whatFind)
        print(start,' ',end)
        lst.append(start)
    print(lst)

printLocations('This is a dish', 'is')

'''Exercise 4.5.1. Make a program scene.py creating a scene with the graphics methods. You are
likely to need to adjust the positions of objects by trial and error until you get the positions you want. Make
sure you have graphics.py in the same directory as your program.'''
from graphics import *
def main():
    winWidth = 500
    winHeight = 500
    win = GraphWin('Draw a Scene', winWidth, winHeight)
    win.setCoords(0, 0, winWidth, winHeight)
    win.setBackground('blue')
    message = Text(Point(winWidth/2, 70), 'Just a scene')
    message.draw(win)
    scene = Oval(Point(30, 350), Point(470, 150))
    scene.setFill("green")
    scene.draw(win)
    message.setText('Click anywhere to quit.')
    message.setTextColor('yellow')
    message.setStyle('italic')
    message.setSize(20)
    win.getMouse()
    win.close()
main()

'''Exercise 4.5.2. Elaborate your scene program so it becomes changeScene.py, and changes one or
more times when you click the mouse (and use win.getMouse()). You may use the position of the mouse
click to affect the result, or it may just indicate you are ready to go on to the next view.'''
from graphics import *
def main():
    winWidth = 500
    winHeight = 500
    win = GraphWin('Draw a Scene', winWidth, winHeight)
    win.setCoords(0, 0, winWidth, winHeight)
    win.setBackground('blue')
    message = Text(Point(winWidth/2, 70), 'Just a scene')
    message.draw(win)
    p1 = Point(30, 350)
    p2 = Point(470, 150)
    scene1 = Oval(p1, p2)
    scene1.setFill("green")
    scene1.draw(win)
    p1 = win.getMouse()
    p2 = win.getMouse()
    scene1.undraw()
    scene2 = Oval(p1, p2)
    scene2.setFill("orange")
    scene2.draw(win)
    p1 = win.getMouse()
    p2 = win.getMouse()
    scene2.undraw()
    scene3 = Oval(p1, p2)
    scene3.setFill("purple")
    scene3.draw(win)
    message.setText('Click anywhere to quit.')
    message.setTextColor('yellow')
    message.setStyle('italic')
    message.setSize(20)
    win.getMouse()
    win.close()
main()


