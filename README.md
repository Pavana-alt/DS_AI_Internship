# DS AI Internship - Python Fundamentals Learning Path

This workspace contains a comprehensive Python fundamentals learning curriculum organized by days, covering basic concepts to file handling and data processing.

## 📁 Directory Structure

### Day-1/
**File:** `Day1_python_fundamentals.py`
- **Purpose:** Introduction to Python basics
- **Content:** Hello World program - first steps in Python
- **Topics:** Basic print statements and syntax

### Day-2/
**File:** `Day2_python_fundamentals.py`
- **Purpose:** Variables, data types, and basic operations
- **Content:** 
  - Variable declaration (int, float, string, boolean)
  - Arithmetic operations using input
  - Calculator logic with conditional statements (if-elif-else)
  - Task 1: Personal greeting with age calculation for 2030
  - Task 2: Bill splitting calculator with type conversion
  - Task 3: Incomplete (for future development)
- **Key Concepts:** Variables, data types, operators, conditional logic

### Day-3/
**File:** `Day3_python_fundamentals.py`
- **Purpose:** Collections - Lists and Tuples
- **Content:**
  - List creation, indexing, and slicing with step values
  - List methods: append(), pop(), sort(), reverse()
  - Tuple creation and immutability
  - Task 1: List manipulation with fruits
  - Task 2: Temperature data analysis with indexing and slicing
  - Task 3: Tuple immutability demonstration
- **Key Concepts:** Lists, tuples, indexing, slicing, list methods

### Day-4/
**File:** `Day4_python_fundamentals.py`
- **Purpose:** Dictionaries and Sets
- **Content:**
  - Dictionary creation, access, and modification
  - Dictionary methods: get(), update(), pop(), items(), keys()
  - Iterating through dictionaries
  - min() and max() functions with keys
  - Set operations and methods: add()
  - Customer purchase analysis with dynamic input
- **Key Concepts:** Dictionaries, sets, key-value pairs, iteration

### Day-5/
**Files:**
- `Day5_python_fundamentals.py`: Functions and scope
- `main.py`: Main application file
- `main1.py`: Alternative main application file
- `math_operations.py`: Utility functions

**Content:**
- Function definition and calling
- Function parameters and return values
- Variable scope (local vs global)
- Multiple return values
- Task 1: Rectangle area and perimeter calculator
- Imported functions from other modules

**Key Concepts:** Functions, parameters, return values, scope, imports

### Day-7/
**Python Scripts:**
- `text_file_demo.py`: Comprehensive file handling examples

**Data Files:**
- `Data.csv`: Employee/contact data (Name, Age, Phone.No)
- `students.csv`: Student performance data (Name, Grade, Status)
- `journal.txt`: Journal entries with names and daily goals
- `Sample.txt`: Sample text file for file handling demonstrations

**Content of `text_file_demo.py`:**
- Basic file operations (write, read)
- Context manager with `with` statement
- Exception handling for FileNotFoundError
- CSV file reading with csv module
- Excel file handling using openpyxl library
- Task 1: Journal entry system - appending user input to journal.txt
- Task 2: Student performance filtering - reading students.csv and filtering passed students
- Task 3: Dynamic file reading with error handling

**Key Concepts:** File I/O, context managers, error handling, CSV processing, Excel handling

## 📊 Sample Data Files

### Data.csv
Contains contact information for 5 people with their phone numbers.

### students.csv
Contains student records with grades and pass/fail status:
- Alice (Grade A, Status: Pass)
- Bob (Grade B, Status: Pass)
- Charlie (Grade F, Status: Fail)

### journal.txt
User-generated journal entries with names and daily goals.

### Sample.txt
Generated sample text file demonstrating write operations.

## 🔧 Dependencies & Requirements

- **Python 3.x**
- **openpyxl library** (for Day-7 Excel file handling)
  - Install: `pip install openpyxl`
- **csv module** (built-in, no installation needed)

## 📚 Learning Path Overview

| Day | Topic | Key Skills |
|-----|-------|-----------|
| 1 | Python Basics | Print, syntax |
| 2 | Variables & Operations | Data types, operators, conditionals |
| 3 | Collections | Lists, tuples, indexing, slicing |
| 4 | Advanced Collections | Dictionaries, sets, iteration |
| 5 | Functions | Definition, parameters, scope, imports |
| 7 | File Handling | File I/O, CSV, Excel, error handling |

## 🎯 Tasks Summary

- **Day 2 Tasks:** Personalized greeting, bill splitter calculator
- **Day 3 Tasks:** List manipulation, temperature analysis, tuple immutability
- **Day 4 Tasks:** Customer purchase tracking with min/max analysis
- **Day 5 Task:** Rectangle calculations using multiple return values
- **Day 7 Tasks:** Journal entry system, student filtering, dynamic file reader

## 🚀 How to Use

1. Navigate to the desired day folder
2. Run the corresponding Python file:
   ```bash
   python Day-X\DayX_python_fundamentals.py
