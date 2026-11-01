import json
# tell which file name to import
file_name = "student.json"

# Setup student variable rules
def print_students(students):
    for student in students:
        print(
            f"{student['L_Name']}, {student['F_Name']} : "
            f"ID = {student['Student_ID']}, Email = {student['Email']}"
        )

# Setup the main rules
def main():
    with open(file_name, "r") as file:
        student_list = json.load(file)

    print("\n--- This is the original Student list. ---")
    print_students(student_list)

# Append the list and add new data
    new_student = {
        "L_Name": "Siggers",
        "F_Name": "Michael",
        "Student_ID": 99887,
        "Email": "msiggers@my.rasyedu.us",
    }
    student_list.append(new_student)

    print("\n-- This is the updated Student list. ---")
    print_students(student_list)

    with open(file_name, "w") as file:
        json.dump(student_list, file, indent=4)

    print("\n[Notification] The student.json file was updated successfully!\n")

# Call main
if __name__ == "__main__":
    main()