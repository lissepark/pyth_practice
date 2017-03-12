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


'''Exercise 1.10.4.2. Write a version of Exercise 1.10.3.2, quotientformat.py, that uses the string
format method to construct the final string.'''
