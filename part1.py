# -*- coding: cp1252 -*-
'''Exercise 1.5.1.1. Figure out how to give Python the string containing the text: I’m happy. Try it.
If you got an error, try it with another type of quotes, and figure out why that one works and not the first.
>>> "I'm happy"
"I'm happy"
'''

''' Exercise 1.5.2.1. Figure out a compact way to get Python to make the string, “YesYesYesYesYes”,
and try it. How about “MaybeMaybeMaybeYesYesYesYesYes” ?
>>> 5*'Yes'
'YesYesYesYesYes'
>>> 3*'Maybee' + 'Yes'*5
'MaybeeMaybeeMaybeeYesYesYesYesYes'
'''

''' Exercise 1.10.3.1. Write a version, add3.py, that asks for three numbers, and lists all three, and
their sum, in similar format to the example above.'''
a = int(input("Enter the first integer, please: "))
b = int(input("Enter the second integer, please: "))
c = int(input("Enter the third integer, please: "))
print('The first integer is:', a)
print('The second integer is:', b)
print('The third integer is:', c)
print('The sum of',a,'and',b,'and',c,'is:', a+b+c)

'''Exercise 1.10.3.2. a. Write a program, quotient.py, that prompts the user for two integers, and
then prints them out in a sentence with an integer division problem like "The quotient of 14 and 3 is
4 with a remainder of 2".'''
d = int(input("Enter the first integer, please: "))
e = int(input("Enter the second integer, please: "))
print('The quotient of', d, 'and', e, 'is', d//e, 'with a remainder of', d%e)

'''Exercise 1.10.4.1. Write a version of Exercise 1.10.3.1, add3f.py, that uses the string format method
to construct the final string.'''
a = int(input("Enter the first integer, please: "))
b = int(input("Enter the second integer, please: "))
c = int(input("Enter the third integer, please: "))
print('The first integer is: {}'.format(a))
print('The second integer is: {}'.format(b))
print('The third integer is: {}'.format(c))
print('The sum of {0} and {1} and {2} is: {3}'.format(a,b,c,a+b+c))

'''Exercise 1.10.4.2. Write a version of Exercise 1.10.3.2, quotientformat.py, that uses the string
format method to construct the final string.'''
d = int(input("Enter the first integer, please: "))
e = int(input("Enter the second integer, please: "))
print('The quotient of {} and {} is {} with a remainder of {}'.format(d,e,d//e,d%e))

'''Exercise 1.11.3.1. Write a program, poem.py, that defines a function that prints a short poem or
song verse. Give a meaningful name to the function. Have the program end by calling the function three
times, so the poem or verse is repeated three times.'''
def songVerse():
    print('nella mente, nel cuore mia')
    print('nei miei giorni e nel tempo mia')
    print('non tremar, non aver paura')
    print("non sei un'avventura e sei mia")

for i in range(1,4):
    songVerse()

'''Exercise 1.11.4.1. Make your own further change to the file and save it as birthdayMany.py: Add a
function call, so Maria gets a verse, in addition to Emily and Andre. Also print a blank line between verses.
(You may either do this by adding a print line to the function definition, or by adding a print line between
all calls to the function.)'''
def happyBirth(person):
    print('Happy birthday to you!')
    print('Happy birthday to you!')
    print('Happy birthday, dear '+person+'!')
    print('Happy birthday to you!')

person1=input('Enter the name: ')
person2=input('Enter the name: ')
def main():
    print(happyBirth(person1))
    print('')
    print(happyBirth(person2))
main()

'''Exercise 1.11.5.1. Modify the program above and save it as quotientProb.py. The new program
should have a quotientProblem function, printing as in the Exercise 1.10.3.2. The main method should test
the function on several sets of literal values, and also test the function with input from the user.'''
def quotientProblem(x, y):
    quot = x//y
    remaind = x%y
    print('The quotient of ', x, 'and ', y, 'is ', quot, 'with a remainder of ', remaind)
    
def main():
    quotientProblem(2, 3)
    quotientProblem(1234567890123, 535790269358)
    a = int(input("Enter an integer: "))
    b = int(input("Enter another integer: "))
    quotientProblem(a, b)

main()

'''Exercise 1.11.6.1. Create quotientReturn.py by modifying quotientProb.py from Exercise 1.11.5.1 so
that the program accomplishes the same thing, but everywhere change the quotientProblem function into
one called quotientString that merely returns the string rather than printing the string directly. Have the
main function print the result of each call to the quotientString function.'''
def quotientProblem(x, y):
    quot = x//y
    remaind = x%y
    result = 'The quotient of ', x, 'and ', y, 'is ', quot, 'with a remainder of ', remaind
    return result
    
def main():
    print(quotientProblem(2, 3))
    print(quotientProblem(1234567890123, 535790269358))
    a = int(input("Enter an integer: "))
    b = int(input("Enter another integer: "))
    print(quotientProblem(a, b))

main()

'''Exercise 1.12.1.1. Write a tiny Python program numDict.py that makes a dictionary whose keys
are the words ’one’, ’two’, ’three’, and ’four’, and whose corresponding values are the numerical equivalents,
1, 2, 3, and 4 (ints, not strings). Include code to test the resulting dictionary by referencing several of the
definitions and printing the results.'''
def numDict():
    sl = dict ()
    sl['one'] = 1
    sl['two'] = 2
    sl['three'] = 3
    sl['four'] = 4
    return sl
def main():
    sl = numDict()
    print(sl['one']+sl['two'])
main()

'''the next'''

