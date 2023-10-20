'''
SIMPLE PRINTING TEXT AND EXPRESSION
print("Hello I am Jopher Joe S. Ribo")
print("mahal na mahal kita RYUJIN" * 10)
print('*' * 10)
        | THAT IS THE EXPRESSION

<----------------------------------------------------------->'''

'''
simple PROPS?

name = 'Jopher Joe'
age = '19'
is_he = True

print(name)

CHALLENGE!!

CREATE 3 VARIABLES FOR THE NAME, AGE, AND IF THE PATIENT IS NEW

We check in a patient named John Smith.
He is 20 years old and  is a new patient.

name = 'John Smith'
age = 20
is_new = True

print (name, age, is_new)


<----------------------------------------------------------->'''

'''
How to recieve input from the user
Example of the expression is x is your variable what is inside of the x is the expression like x = ('1' + '1')

name = input('What is your name? ')
print ('Hi ' + name)

CHALLENGE!!

Ask two questions: person's name and favourite color.
Then, print a message like "Mosh likes blue"


name = input ('what is your name? ')
color = input ('what is your favourite color? ')

print(name + " likes " + color)


<----------------------------------------------------------->'''

'''
Type Conversion
birth_year = input ('Birth Year: ')
age = 2023 - int(birth_year)
print(age)

CHALLENGE!!

Ask a user their weight (in pounds), convert it to kilograms and print on the terminal


pounds = input('What is your weight?(in pounds) ')
print(type(pounds))
kg = 0.453592 * int(pounds)
print(type(kg))
print(kg)

<----------------------------------------------------------->'''

'''String


course  = 'Python is for beginners'
'the array is 0123456789 and for the end is -1-2-3-4-5'

print(course[1:])
print(course[0:] = it will include all
print (course[1:] = int will remove the 1st

'and also you can do this'

course = 'Jopher'
another = course[:5]

print(another)

name = 'Jopher'
print(name[1:-1])

<----------------------------------------------------------->'''

'''Formatted Strings(so the f means is a "formatted strings")
first_name = 'Jopher'
last_name = 'Ribo'
message = (first_name + ' [' + last_name + '] ' + 'is a coder' )
msg = f'{first_name} [{last_name}] is a coder'
print(msg)
<----------------------------------------------------------->'''

'''String Methods
len is a lenght?
course = 'Python for beginners'
print(course.upper())

name = input("What is you fucking name?")
kg = input("what is your weight?")
color = input("what is you favourite color?")
weight = 0.453592 * int(str(kg))
msg = f'{name} and my favourite color is {color} and your weight is {weight}'
print("your length in name is", len(name))
print("and your favourite color length is",len(color))
print (weight)
print(msg)

name = input('what is your name? ')
kg = input('what is your weight?')
weight = 10000000000 + int(kg)

msg = f'Your name is {name} and your weight is {weight}'

print(msg)

course = 'Python for Beginners'
print('Jopher' in course)
print(course.replace('B', 'U'))
print(course.upper())
print(course)

x = 10 + 2 * 3 ** 2
print(x)

is_hot = False
is_cold = True

if is_hot:
    print("Yeah it's hot")
elif is_cold:
    print("Ryujin doesn't love me anymore")
else:
    print("YEAH ITS RYUJIN FUCKING HOT")
print("But I always love her")


price = 100000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f'Down Payment: ${down_payment}')

weather = True
air = False

if weather or not air:
    print("Yeah it's beautiful")

temperature = 30

if temperature != 30:
    print("It's hot today")
elif temperature == 10:
    print("It's cold Today")
else:
    print("It's neither hot nor cold")'''

name = 3

if name > 50:
    print("name must be at least 3 characters long")
elif name > 50:
    print("name can be a maximum of 50 characters")
else:
    print("name looks good")



