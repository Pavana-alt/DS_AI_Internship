age=21
print(age)
height=5.8
print(height)   
name="Pavana"
print(name)
is_student=True
print(is_student)


a=int(input("Enter a value:"))
b=int(input("Enter another value:") )
operator=input("Enter the operator(+,-,*,/,%):")

if operator=="+":
    sum=a+b
    print("The sum of entered numbers is:",sum,"\n")
elif operator=="-":
    diff=a-b
    print("The difference of entered numbers is:\n",diff,"\n")
elif operator=="*":
    prod=a*b
    print("The product of entered numbers is:\n",prod,"\n")
elif operator=="/":
    quotient=a/b
    print("The quotient of entered numbers is:\n",quotient,"\n")
elif operator=="%":
    modulus=a%b
    print("The modulus of entered numbers is:\n",modulus,"\n")
else:
    print("Invalid operator\n")   

# #Task 1:
name=input("Enter your name:")
print("Welcome",name+"!\n")
age=int(input("Enter your age:"))
age_2030=age+4
print(f"How are you, {name}!,you will be {age_2030} years old in 2030!\n")


# #Task 2:
total_bill=float(input("Enter the total bill amount:"))
peoples=int(input("Enter number of people to split the bill:"))
total_share=total_bill/peoples
print(f"Total Bill: {total_bill}. Each person pays: {total_share}")
print(type(total_bill))
print(type(peoples))
print(type(total_share))

#Task 3:
item_name="Laptop"
quantity=5
price=799.99
in_stock=True
print("Item:",item_name,", Qty:", quantity,", Price:", price,", Available:", in_stock)
total_cost=quantity*price
print(f"Total cost is: ${total_cost}")

