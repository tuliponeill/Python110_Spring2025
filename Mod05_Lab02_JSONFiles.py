# ------------------------------------------------------------------------------------------ #
# Title: Working With Dictionaries And Files
# Desc: Shows how work with dictionaries and files when using a table of data
# Change Log: (Who, When, What)
#   TONeill, 05/19/2025, Created script
# ------------------------------------------------------------------------------------------ #

# Import libraries
import json

# Define the program's constants
FILE_NAME: str = "MyLabData.json"
MENU: str = """
---- Student GPAs -------------------------------
  Select from the following menu:  
    1. Show current student data. 
    2. Enter new student data.
    3. Save data to a file.
    4. Exit the program.
--------------------------------------------------
"""

# Define the program's variables
student_first_name: str = ""  # Holds the first name of a student entered by the user.
student_last_name: str = ""  # Holds the last name of a student entered by the user.
student_gpa: float = 0.0  # Holds the GPA of a student entered by the user.
message: str = ""  # Holds a custom message string
menu_choice: str = ""   # Hold the choice made by the user.
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
file_data: str = ""  # Holds combined string data separated by a comma.
file = None  # Not using type hint helps PyCharm, so we won't use it going forward

# When the program starts, read the file data into a list of dictionary rows (table)
#file = open(FILE_NAME, "r")

# Extract the data from the file
#for row in file.readlines():

    # Transform the data from the file
    #student_data = row.split(",")
    #student_data = {"First Name": student_data[0],
                    #"Last Name": student_data[1],
                    #"GPA": float(student_data[2].strip())}

    # Load it into the collection (list of lists)
    #students.append(student_data)
#file.close()

# Open the JSON file, dump data into students table variable, close file
file = open(FILE_NAME, "r")
students = json.load(file)
file.close()

# Repeat the follow tasks
while True:
    print(MENU)
    menu_choice = input("Please select from the menu: ")
    print()

    # display the table's current data
    if menu_choice == "1":
        print("-"*50)
        for student in students:
            if student["GPA"] >= 4.0:
                message = "{} {} earned an A with a GPA of {:.2f}."
            elif student["GPA"] >= 3.0:
                message = "{} {} earned a B with a GPA of {:.2f}."
            elif student["GPA"] >= 2.0:
                message = "{} {} earned a C with a GPA of {:.2f}."
            elif student["GPA"] >= 1.0:
                message = "{} {} earned a D with a GPA of {:.2f}."
            else:
                message = "{} {}'s GPA of {:.2f} did not earn a passing grade."
            print(message.format(student["First Name"],student["Last Name"],student["GPA"]))
        print("-"*50)

    # Add data to the table
    elif menu_choice == "2":
        student_first_name = input("Student first name: ")
        student_last_name = input("Student last name: ")
        student_gpa = float(input("Student GPA: "))
        student_data = {"First Name": student_first_name,
                        "Last Name": student_last_name,
                        "GPA": student_gpa}
        students.append(student_data)
        print("Student data added successfully.")
        print("-"*50)
        continue

    # Save the data to the CSV file
    #elif menu_choice == "3":
        #file = open(FILE_NAME, "w")
        #for student in students:
            #file.write(f"{student["First Name"]},{student["Last Name"]},{student["GPA"]}\n")
        #file.close()
        #print("Student data saved to file successfully.")
        #print("-"*50)
        #continue

    # Save the data to the JSON file
    elif menu_choice == "3":
        file = open(FILE_NAME, "w")
        json.dump(students, file)
        file.close()
        print("Student data saved to file successfully.")
        print("-" * 50)
        continue

    # Exit the program
    elif menu_choice == "4":
        print("Thank you for using this program.")
        break