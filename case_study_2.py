'''
# WAP to take a dict from the user and print the sum of values
d = eval(input('Enter the dictionary:'))
print('Dictionary is:', d)
print('Sum of the values from d is:', sum(d.values()))
------------------------------------------------------------
WAP to find a number of occurrences of each letter present in the given string

s = input('Enter the string:')
d = {}
for i in s:
    d[i] = d.get(i, 0)+1
print(d)
--------------------------------------------------------------------
WAP to find out number of occurrences of each vowel present in the given string
input:

'python a is simple'

vowels = a,i'o'u'e

output expected:
o present 1 times
a present 1 times
i present 2 times
e present 1 times
----------------------------------------------------
word = input('Enter any word:')
vowels = ['a', 'i', 'o', 'u', 'e']
d = {}
for x in word:
    if x in vowels:
        d[x] = d.get(x, 0)+1
for key in sorted(d):
    print(key, 'presents', d[key], 'times')
----------------------------------------------------------
WAP to accept student name, marks from user and create a dict.
Also display the student name and marks

Ask students name and then display marks
--------------------------------------
n = int(input('Enter the number of students:'))
for i in range(n):
    name = input('Enter the name:')
    marks = input('Enter your marks:')
    print('Your name is:',name, 'marks obtained:', marks)
    print('---------------------------------------------')
-------------------------------------------------------------
'''
import sys
n = int(input('Enter the number of students:'))
d = {}
for i in range(n):
    name = input('Enter the name:')
    marks = input('Enter your marks:')
    d[name] = marks
print(d)
while True:
    nm = input('Enter the name to search:')
    if nm in d:
        print('Marks obtained by', nm, ':', d[nm])
    else:
        print('Candidate not found')
        #sys.exit()
        break



















