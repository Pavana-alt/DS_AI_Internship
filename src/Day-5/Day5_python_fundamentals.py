#Functions in Python
def greet():
    print("Hello everyone!, Welcome to the internship")
greet()
 
#Function with parameters
def add_numbers(a,b):
    return a+b
result=add_numbers(5,3)
print("The sum of 5 and 3 is:",result)

#Variable scope
x=10
def show_value():
    x=5
    print("Local variable x:",x)
show_value()
print("Global variable x:",x)

#creating multiple functions
cars="BMW"
def display_cars():
    Bike="Ducati"
    Laptop="Dell"
print("Ducati are very attractive")
print("Dell is a popular brand")
display_cars()
print("Cars brand is:",cars)

#importing functions from another file
def multiply(a,b):
    return a*b

#Task-1
def calc_rectangle(length, width):
    area=length*width
    perimeter=2*(length+width)
    return area, perimeter
area=float(input("Enter the length of the rectangle: "))
width=float(input("Enter the width of the rectangle: "))
area, perimeter=calc_rectangle(area, width)
print(f"Area: {area}, Perimeter: {perimeter}")


