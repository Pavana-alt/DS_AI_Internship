#working with pandas series
import pandas as pd

s1 = pd.Series([10, 20, 30, 40])
s2 = pd.Series([10, 20, 30], index=['a', 'b', 'c'])

print(s1)
print(s2)

# Accessing elements in a Series
import pandas as pd
marks = pd.Series([85, 90, 78], index=['Math', 'Physics', 'Chemistry'])

print(marks['Math'])
print(marks[['Math', 'Chemistry']])

# Filtering a Series
import pandas as pd 
scores = pd.Series([45, 67, 89, 34, 90])

passed = scores[scores > 60]
print(passed)


# Handling missing data in a Series
import pandas as pd
data = pd.Series([10, None, 30, None])

print(data.isnull())
print(data.fillna(0))

#Another example
import pandas as pd
data=pd.Series([20,None,None,40,39])

print(data.isnull())
print(data.fillna(6))


# String operations on Series
import pandas as pd
names = pd.Series(['Alice', 'bob', 'CHARLIE'])

print(names.str.lower())
print(names.str.contains('a'))

#Task-1
import pandas as pd
products = pd.Series([700, 150, 300], index=["Laptop", "Mouse", "Keyboard"])
laptop_price = products["Laptop"]
first_two = products.iloc[0:2]
print("Full Series:")
print(products)
print("\nPrice of Laptop:")
print(laptop_price)
print("\nFirst two products:")
print(first_two)

#Task-2
import pandas as pd
grades=pd.Series([85,None,92,45,None,78,55])
print("Original Series:")
print(grades)
print("\nMissing values in the series:")
print(grades.isnull())
print("\nSeries with missing values filled with 0:")
print(grades.fillna(0))
filtered_grades = grades[grades > 60]
print("\nGrades greater than 60:", filtered_grades)

#Task-3
import pandas as pd
usernames = pd.Series(['Alice', 'bOB', 'Charlie_Data','daisy'])
print("Usernames with stripped whitespace:")
print(usernames.str.strip())
print("\nUsernames in lowercase:")  
print(usernames.str.lower())
print("\nUsernames containing 'a':")
print(usernames.str.contains('a'))

