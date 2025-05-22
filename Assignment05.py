# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot, 1/1/2030, Created script
#   TONeill, 05/21/2025, Created script
# ------------------------------------------------------------------------------------------ #

# Import libraries
import json

# Define the Data Constants
MENU: str = """
---- Course Registration Program --------
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
-----------------------------------------
"""
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
student_first_name: str = "" # Holds the first name of a student entered by the user.
student_last_name: str = "" # Holds the last name of a student entered by the user.
course_name: str = "" # Holds the name of a course entered by the user.
student_data: dict = {} # One row of student data.
students: list = [] # A table of student data
#csv_data: str = "" # Holds combined CSV data.
file = None # Holds a reference to an opened file.
menu_choice: str # Holds the menu choice made by the user.

# When the program starts, read the file data into a list of dictionaries (table)
try:
    file = open(FILE_NAME, "r")
    students = json.load(file)
    file.close()
except FileNotFoundError as e:
    print("Please check that file exists.\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
except json.decoder.JSONDecodeError as e:
    print("There was an error parsing the file.\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
except Exception as e:
    print("There was a non-specific error!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
finally:
    if file.closed == False:
        file.close()

# Present and Process the data
while True:

    # Present the menu of choices
    print(MENU)
    menu_choice = input("Choose a menu option (1,2,3,4): ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        print("To register a student, please enter the following information...")
        try:
            student_first_name = input("Student first name: ")
            if not student_first_name.isalpha():
                print("First name must only contain letters. Please try again.")
                continue

            student_last_name = input("Student last name: ")
            if not student_last_name.isalpha():
                print("Last name must only contain letters. Please try again.")
                continue

        except ValueError as e:
            print(e)  # Prints the custom message
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
            continue
        except Exception as e:
            print("There was a non-specific error!\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
            continue

        course_name = input("Course name: ")
        student_data = {"First Name": student_first_name,
                        "Last Name": student_last_name,
                        "Course": course_name}
        students.append(student_data)
        print(f"{student_first_name} {student_last_name} has successfully been registered for {course_name}.")
        continue

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-"*50)
        for student in students:
            print(f"{student["First Name"]},{student["Last Name"]},{student["Course"]}")
        print("-"*50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file)
            file.close()
            print("-" * 50)
            print("The following data has been saved to file:")
            for student in students:
                print(f"{student["First Name"]},{student["Last Name"]},{student["Course"]}")
            print("-" * 50)
        except TypeError as e:
            print("Please check that the data is a valid JSON format\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
        except Exception as e:
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
        finally:
            if file.closed == False:
                file.close()
            continue

    # Stop the loop
    elif menu_choice == "4":
        break
    else:
        print("Please only choose option 1, 2, 3, or 4")

print("Thank you for using this program.")