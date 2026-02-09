#file handling in python
file=open("Sample.txt","w")
file.write("Hello,this is a file handling example in python.")
file.close()
file=open("Sample.txt","r")
content=file.read()
print(content)
file.close()

#context manager with statement and open function
with open("Sample.txt","r") as file:
    content=file.read()
    print(content)

#using try-except block to handle file not found error
try:
    with open("Missing.txt","r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found. Please check the file name and try again.")

#reading a csv file
import csv
with open("Data.csv","r") as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)

#excel file handling using openpyxl library
import openpyxl
workbook = openpyxl.load_workbook("data1.xlsx")
sheet = workbook.active  
for row in sheet.iter_rows(values_only=True):
    print(row)

#Task-1
name=input("Enter your name: ")
daily_goal=input("Enter your daily goal: ")
with open("journal.txt","a") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Daily Goal: {daily_goal}\n")
    print("Journal entry added successfully.")

#Task-2
import csv
with open("students.csv","r") as file:
    reader=csv.reader(file)
    print("Students who passed:")
    for row in reader:
        if row[2] == "Pass":
            print(row[0])

#Task-3
filename = input("Enter the filename: ")

try:
    with open(filename, "r") as file:
        content = file.read()
        print("File content:\n")
        print(content)

except FileNotFoundError:
    print("Oops! That file doesn't exist yet.")
