from inspect import Parameter


num1 = 42-- variable declaration
um2 = 2.3-- variable declaration
boolean = True-boolean
string = 'Hello World'---string declaration
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']-- List 
            - initialize 
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}-- #Dictionary  - initialize
fruit = ('blueberry', 'strawberry', 'banana')- - Tuples initialize
print(type(fruit))-type check
print(pizza_toppings[1])-access list values
pizza_toppings.append('Mushrooms')-add list values
print(person['name'])-access dictionary values
person['name'] = 'George'-change dictionary values
person['eye_color'] = 'blue'- add key values to dictionary values
print(fruit[2])-access Tuples values
if num1 > 45:-if conditional statement
    print("It's greater")-log statement
else:else conditional statement
    print("It's lower")-log statement

if len(string) < 5:     conditional statement
    print("It's a short word!")-log statement if True
elif len(string) > 15:-if conditional statement is false log this.
    print("It's a long word!")-log statement part of of elif
else:if either if or elif statement is false
    print("Just right!")-log statement
for x in range(5): for loop
    print(x)-varible x printed 5x
for x in range(2,5):-for loop
    print(x)
for x in range(2,10,3):for loop
    print(x)
x = 0-defined variable
while(x < 5):while loop
    print(x)
    x += 1

pizza_toppings.pop()-
pizza_toppings.pop(1)

print(person)-log dictionary
person.pop('eye_color')
print(person)

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()-function
print_hello_x_or_ten_times(4)-function with Parameter


"""
Bonus section- --- multiline comment section

"""

son['favorite_team'])-single comment section
print(pizza_toppings[7])-single comment section
  print(boo print(num3)-        single comment section - NameError: name <variable name> is not #defined

num3 = 72-           single comment section
fruit[0] = 'cranberry'-     single comment section
print(perlean)-single comment section
fruit.append('raspberry')-single comment section
fruit.pop(1)-single comment section