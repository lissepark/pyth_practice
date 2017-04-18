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



