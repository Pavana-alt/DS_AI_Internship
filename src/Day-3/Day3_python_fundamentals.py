#Lists
numbers = [10, 20, 30, 40]
#Tuples
coordinates = (5, 10)
print("List of numbers:", numbers)
print("Coordinates:", coordinates)

a=[100,200,300,400,500,600,700]
range=a[-3:-1]
print("Range is:",range)
print(a[1:6:2])

print(a[-5:-1:2])

marks=[85,90,78,92,88]
marks.append(95)
print(marks)
marks.pop(2)  
print(marks)
marks.sort() 
print(marks) 
marks.reverse()
print(marks)

#Task 1
list=["Apple","Banana","Carrot","Dates"]
print(list)
list.append("Eggs")
print(list)
list.remove("Banana")
print(list)
list.sort()
print(list)

#Task-2
temperatures=[22, 24, 25, 28, 30, 29, 27, 26, 24, 22]
print("First reading:",temperatures[0])
print("Last reading:",temperatures[-1])
print("Afternoon Peak readings:",temperatures[3:6])
print("Last three hours readings:",temperatures[-3:])

#Task-3
screen_res=(1920,1080)
print("Current resolution:1920*1080")
#screen_res[0]=1280
print("Tuples cannot be modified.")
