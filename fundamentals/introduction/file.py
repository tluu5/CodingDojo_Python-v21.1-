# data types, numbers
num1 = 42
num2 = 2.3
# data types, boolean
boolean = True
# strings
string = 'Hello World'
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
fruit = ('blueberry', 'strawberry', 'banana')
print(type(fruit))
print(pizza_toppings[1])
# dictionary initialize
pizza_toppings.append('Mushrooms')
print(person['name'])
# change value
person['name'] = 'George'
person['eye_color'] = 'blue'
print(fruit[2])
# conditional, if
if num1 > 45:
    print("It's greater")
# else 
else:
    print("It's lower")
# else if
if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")
# while loop
for x in range(5):
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)
x = 0
while(x < 5):
    print(x)
    x += 1

pizza_toppings.pop()
pizza_toppings.pop(1)
# add value
print(person)
person.pop('eye_color')
print(person)
# function parameter
for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break
# arguemnt
def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()
# argument
def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)
# argument
def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)