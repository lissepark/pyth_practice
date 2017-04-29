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

'''Exercise 4.12.1. Write a program ranges.py that uses the range function to produce the sequnce
1, 2, 3, 4, and then print it. Also prompt the user for an integer n and print the sequnce 1, 2, 3, ... , n –
including n. Hint: 8 Finally use a simple repeat loop to find and print five randomly chosen numbers from
the range 1, 2, 3, ... , n .'''
import random

s = input('Please type an number: ')
print(s)
k = int(s)

def simpleRange(n):
    for t in range (1,n+1):
        print(t)
print('------------------------------')
def randRange(n):
    for t in range (5):
        print(random.randrange(1,n+1))

def mainRand(k):
    simpleRange(k)
    print('-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-')
    randRange(k)

mainRand(k)

'''Exercise 5.0.2. Make the following programs in sequence. Be sure to save the programs in the same
directory as where you start the idle shortcut and where you have all the sample text files:
* a. printUpper.py: read the contents of the sample2.txt file and print the contents out in upper case. (This
should use file operations and should work no matter what the contents are in sample2.txt. Do not assume
the particular string written by nextFile.py!)
* b. fileUpper.py: prompt the user for a file name, read and print the contents of the requested file in upper
case.
* c. copyFileUpper: modify fileUpper.py to write the upper case string to a new file rather than printing
it. Have the name of the new file be dynamically derived from the old name by prepending ’UPPER’ to
the name. For example, if the user specified the file sample.txt (from above), the program would create
a file UPPERsample.txt, containing ’MY FIRST OUTPUT FILE!’. When the user specifies the file name
stuff.txt, the resulting file would be named UPPERstuff.txt.'''
fileOut = open('sample2.txt','r')
context = fileOut.read()
print(context.upper())
inp = input('Type, please, the file name')
fileOut2 = open(inp,'r')
context2 = fileOut2.read()
print(context2.upper())

fileInUpper = open('UPPER'+inp,'w')
fileInUpper.write(context2.upper())
fileInUpper.close()

'''Exercise 5.0.3. Write madlib3.py, a small modification of madlib2.py, requiring only a modification
to the main function of madlib2.py. Your madlib3.py should prompt the user for the name of a file that
should contain a madlib format string as text (with no quotes around it). Read in this file and use it as the
format string in the tellStory function. This is unlike in madlib2.py, where the story is a literal string
coded directly into the program called originalStory. The tellstory function and particularly the getKeys
function were developed and described in detail in this tutorial, but for this exercise there is no need to
follow their inner workings - you are just a user of the tellstory function (and the functions that it calls).
You do not need to mess with the code for the definition of tellStory or any of the earlier supporting
functions. The original madlib string is already placed in a file jungle.txt, that is in this format as an
example. With the Idle editor, write another madlib format string into a file myMadlib.txt. If you earlier
created a file myMadlib.py, then you can easily extract the story from there (without the quotes around it).
Test your program both with jungle.txt and your new madlib story file.'''
def getKeys(formatString): # change: returns a set
    '''formatString is a format string with embedded dictionary keys.
    Return a set containing all the keys from the format string.'''
    keyList = list()
    end = 0
    repetitions = formatString.count('{')
    for i in range(repetitions):
        start = formatString.find('{', end) + 1
        end = formatString.find('}', start)
        key = formatString[start : end]
        keyList.append(key) # may add duplicates
    return set(keyList) # removes duplicates: no duplicates in a set
def addPick(cue, dictionary): # from madlib.py
    '''Prompt the user and add one cue to the dictionary.'''
    prompt = 'Enter an example for ' + cue + ': '
    dictionary[cue] = input(prompt)
def getUserPicks(cues):
    '''Loop through the collection of cue keys and get user choices.
    Return the resulting dictionary.
    '''
    userPicks = dict()
    for cue in cues:
        addPick(cue, userPicks)
    return userPicks
def tellStory(story):
    '''story is a format string with Python dictionary references embedded,
    in the form {cue}. Prompt the user for the mad lib substitutions
    and then print the resulting story with the substitutions.
    '''
    cues = getKeys(story)
    userPicks = getUserPicks(cues)
    print(story.format(**userPicks))
def main():
    fileOut = open('UPPERsample.txt','r')
    originalStory = fileOut.read()
    tellStory(originalStory)
main()
