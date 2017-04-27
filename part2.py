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

'''Exercise 4.8.1. Save backAndForth3.py to the new name backAndForth4.py. Add a triangular
nose in the middle of the face in the makeFace function. Like the other features of the face, make sure the
position of the nose is relative to the center parameter. Make sure the nose is included in the final list of
elements of the face that get returned.'''
from graphics import *
import time
def moveAll(shapeList, dx, dy):
    for shape in shapeList:
        shape.move(dx, dy)
def moveAllOnLine(shapeList, dx, dy, repetitions, delay):
    for i in range(repetitions):
        moveAll(shapeList, dx, dy)
        time.sleep(delay)
def makeFace(center, win):
    head = Circle(center, 25)
    head.setFill("yellow")
    head.draw(win)
    eye1Center = center.clone() # face positions are relative to the center
    eye1Center.move(-10, 5)
    # locate further points in relation to others
    eye1 = Circle(eye1Center, 5)
    eye1.setFill('blue')
    eye1.draw(win)
    eye2End1 = eye1Center.clone()
    eye2End1.move(15, 0)
    eye2End2 = eye2End1.clone()
    eye2End2.move(10, 0)
    eye2 = Line(eye2End1, eye2End2)
    eye2.setWidth(3)
    eye2.draw(win)
    mouthCorner1 = center.clone()
    mouthCorner1.move(-10, -10)
    mouthCorner2 = mouthCorner1.clone()
    mouthCorner2.move(20, -5)
    mouth = Oval(mouthCorner1, mouthCorner2)
    mouth.setFill("red")
    mouth.draw(win)
    #nose
    noseP1 = center.clone()
    noseP1.move(-3,0)
    noseP2 = noseP1.clone()
    noseP2.move(6,0)
    noseP3 = noseP2.clone()
    noseP3.move(-3,-4)
    nose = Polygon(noseP1,noseP2,noseP3)
    nose.setFill("green")
    nose.draw(win)
    return [head, eye1, eye2, mouth,nose]
def main():
    winWidth = 300
    winHeight = 300
    win = GraphWin('Back and Forth', winWidth, winHeight)
    win.setCoords(0, 0, winWidth, winHeight) # make right side up coordinates!
    rect = Rectangle(Point(200, 90), Point(220, 100))
    rect.setFill("blue")
    rect.draw(win)
    faceList = makeFace(Point(40, 100), win)
    faceList2 = makeFace(Point(150,125), win)
    stepsAcross = 46
    dx = 5
    dy = 3
    wait = .05
    for i in range(3):
        moveAllOnLine(faceList, dx, 0, stepsAcross, wait)
        moveAllOnLine(faceList, -dx, dy, stepsAcross//2, wait)
        moveAllOnLine(faceList, -dx, -dy, stepsAcross//2, wait)
    Text(Point(winWidth/2, 20), 'Click anywhere to quit.').draw(win)
    win.getMouse()
    win.close()
main()

'''Exercise 4.8.2. Make a program faces.py that asks the user to click the mouse, and then draws
a face at the point where the user clicked. Elaborate this with a simple repeat loop, so a face appears for
each of 6 clicks.'''
from graphics import *
import time
def moveAll(shapeList, dx, dy):
    for shape in shapeList:
        shape.move(dx, dy)
def moveAllOnLine(shapeList, dx, dy, repetitions, delay):
    for i in range(repetitions):
        moveAll(shapeList, dx, dy)
        time.sleep(delay)
def makeFace(winWidth,win):
    clickCenter = Text(Point(winWidth/2, 60), 'Click anywhere to draw face in that position.')
    clickCenter.draw(win)
    center = win.getMouse()
    clickCenter.undraw()
    head = Circle(center, 25)
    head.setFill("yellow")
    head.draw(win)
    eye1Center = center.clone() # face positions are relative to the center
    eye1Center.move(-10, 5)
    # locate further points in relation to others
    eye1 = Circle(eye1Center, 5)
    eye1.setFill('blue')
    eye1.draw(win)
    eye2End1 = eye1Center.clone()
    eye2End1.move(15, 0)
    eye2End2 = eye2End1.clone()
    eye2End2.move(10, 0)
    eye2 = Line(eye2End1, eye2End2)
    eye2.setWidth(3)
    eye2.draw(win)
    mouthCorner1 = center.clone()
    mouthCorner1.move(-10, -10)
    mouthCorner2 = mouthCorner1.clone()
    mouthCorner2.move(20, -5)
    mouth = Oval(mouthCorner1, mouthCorner2)
    mouth.setFill("red")
    mouth.draw(win)
    #nose
    noseP1 = center.clone()
    noseP1.move(-3,0)
    noseP2 = noseP1.clone()
    noseP2.move(6,0)
    noseP3 = noseP2.clone()
    noseP3.move(-3,-4)
    nose = Polygon(noseP1,noseP2,noseP3)
    nose.setFill("green")
    nose.draw(win)
    return [head, eye1, eye2, mouth,nose]
def main():
    winWidth = 300
    winHeight = 300
    win = GraphWin('Back and Forth', winWidth, winHeight)
    win.setCoords(0, 0, winWidth, winHeight)
    rect = Rectangle(Point(200, 90), Point(220, 100))
    rect.setFill("blue")
    rect.draw(win)
    for r in range(6):
        faceList = makeFace(winWidth,win)
    stepsAcross = 46
    dx = 5
    dy = 3
    wait = .05
    for i in range(3):
        moveAllOnLine(faceList, dx, 0, stepsAcross, wait)
        moveAllOnLine(faceList, -dx, dy, stepsAcross//2, wait)
        moveAllOnLine(faceList, -dx, -dy, stepsAcross//2, wait)
    Text(Point(winWidth/2, 20), 'Click anywhere to quit.').draw(win)
    win.getMouse()
    win.close()
main()

'''Exercise 4.8.3. Animate two faces moving in different directions at the same time in a program
move2Faces.py. You cannot use the moveAllOnLine function. You will have to make a variation of your
own. You can use the moveAll function separately for each face. Hint: imagine the old way of making an
animated cartoon. If each face was on a separate piece of paper, and you wanted to animate them moving
together, you would place them separately, record one frame, move them each a bit toward each other, record
another frame, move each another bit toward each other, record another frame, .... In our animations “record
a frame” is replaced by a short sleep to make the position visible to the user. Make a loop to incorporate
the repetition of the moves.'''
from graphics import *
import time
def moveAll(shapeList, dx, dy):
    for shape in shapeList:
        shape.move(dx, dy)
def makeFace(winWidth,win):
    clickCenter = Text(Point(winWidth/2, 60), 'Click anywhere to draw face in that position.')
    clickCenter.draw(win)
    center = win.getMouse()
    clickCenter.undraw()
    head = Circle(center, 25)
    head.setFill("yellow")
    head.draw(win)
    eye1Center = center.clone() # face positions are relative to the center
    eye1Center.move(-10, 5)
    # locate further points in relation to others
    eye1 = Circle(eye1Center, 5)
    eye1.setFill('blue')
    eye1.draw(win)
    eye2End1 = eye1Center.clone()
    eye2End1.move(15, 0)
    eye2End2 = eye2End1.clone()
    eye2End2.move(10, 0)
    eye2 = Line(eye2End1, eye2End2)
    eye2.setWidth(3)
    eye2.draw(win)
    mouthCorner1 = center.clone()
    mouthCorner1.move(-10, -10)
    mouthCorner2 = mouthCorner1.clone()
    mouthCorner2.move(20, -5)
    mouth = Oval(mouthCorner1, mouthCorner2)
    mouth.setFill("red")
    mouth.draw(win)
    noseP1 = center.clone()
    noseP1.move(-3,0)
    noseP2 = noseP1.clone()
    noseP2.move(6,0)
    noseP3 = noseP2.clone()
    noseP3.move(-3,-4)
    nose = Polygon(noseP1,noseP2,noseP3)
    nose.setFill("green")
    nose.draw(win)
    return [head,eye1,eye2,mouth,nose]
def main():
    winWidth = 300
    winHeight = 300
    win = GraphWin('Back and Forth', winWidth, winHeight)
    win.setCoords(0, 0, winWidth, winHeight)
    faceList1 = makeFace(winWidth,win)
    faceList2 = makeFace(winWidth,win)
    stepsAcross = 50
    dx1 = 5
    dy1 = 3
    wait1 = .05
    dx2 = -3
    dy2 = -2
    wait2 = .04
    for o in range(stepsAcross):
        moveAll(faceList1, dx1, dy1)
        moveAll(faceList2, dx2, dy2)
        time.sleep(wait1)
    Text(Point(winWidth/2, 20), 'Click anywhere to quit.').draw(win)
    win.getMouse()
    win.close()
main()

'''

'''
