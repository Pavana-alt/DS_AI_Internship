a={"Name":"John","Age":30}
print(a)

Student={"Name":"Pavana",
         "Age":21,
         "Course":"MCA"
         }
print(Student["Name"])
Student["Age"]=22
Student["City"]="Mangalore"
print(Student)

marks={"Maths":80,"Science":75,"English":85}
print(marks.get("Maths"))
print(marks.get("History",0))
marks.update({"History":90})
marks.pop("Science")
for subject, score in marks.items():
    print(subject,score)

purchases={"Alice":250,
              "Bob":400,
              "Charlie":150
              }
for name,amount in purchases.items():
    print(f"{name} made a purchase of ₹{amount}.")

print("Total customers:",len(purchases))
print("Customer names:",purchases.keys())

n=int(input("Enter the number of customers: "))
user_purchases={}
for i in range(n):
    name=input("Enter customer name: ")
    amount=int(input(f"Enter purchase amount for {name}: "))
    user_purchases[name]=amount
    print("Customer purchase data:",user_purchases)

top_customer=max(user_purchases, key=user_purchases.get)
print("Top spending customer is:",top_customer)

min_customer=min(user_purchases, key=user_purchases.get)
print("Minimum spending customer is:",min_customer)

num={1,2,3,3,4,5}
print(num)
num.add(6)
print(num)

A={1,2,3,4}
B={3,4,5,6}
print(A|B)
print(A&B)
print(3 in A)

#Task-1
contacts={"Pavana":"9034256738",
          "Adithi":"7823145267",
          "Ram":"9067543214"}
print(contacts)
contacts["Sita"]="9876543210"
print(contacts)
contacts.update({"Adithi":"9087653456"})
print("Contact updated successfully")
existing_contacts=contacts.get("Ram","Contact not found")
missing_contact=contacts.get("Laxman","Contact not found")
print("Safe lookups:")
print("Ram's contact:",existing_contacts)
print("Laxman's contact:",missing_contact)  

print("All contacts:")
for name, number in contacts.items():
    print(f"Contact: {name} | Phone Number: {number}")


#Task-2
raw_logs=["ID01","ID02","ID01","ID05","ID02","ID08","ID01"]
unique_users=set(raw_logs)
print("Unique users are:",unique_users)
print("Is ID05 in the logs?", "ID05" in unique_users)
print("Length of original list:", len(raw_logs))
print("Length of the unique set:", len(unique_users))

#Task-3
friend_a={"Python","Cooking","Hiking","Movies"}
friend_b={"Hiking","Gaming","Photography","Python"}

Common_interests=friend_a & friend_b
All_interests=friend_a | friend_b
Unique_interests_a=friend_a - friend_b
print("Common interests:", Common_interests)
print("All interests:", All_interests)
print("Unique interests in friend_a:", Unique_interests_a)
