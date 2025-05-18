
students = {}

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    grade = input("Enter Grade: ")
    students[roll] = {'name': name, 'age': age, 'grade': grade}
    print("Student added successfully!\n")

def display_students():
    if not students:
        print("No student records found.\n")
        return
    print("Student Records:")
    for roll, info in students.items():
        print(f"Roll: {roll}, Name: {info['name']}, Age: {info['age']}, Grade: {info['grade']}")
    print()

def search_student():
    roll = input("Enter Roll Number to search: ")
    if roll in students:
        print(f"Student Found: {students[roll]}\n")
    else:
        print("Student not found.\n")

def update_student():
    roll = input("Enter Roll Number to update: ")
    if roll in students:
        name = input("Enter New Name: ")
        age = input("Enter New Age: ")
        grade = input("Enter New Grade: ")
        students[roll] = {'name': name, 'age': age, 'grade': grade}
        print("Student record updated.\n")
    else:
        print("Student not found.\n")

def delete_student():
    roll = input("Enter Roll Number to delete: ")
    if roll in students:
        del students[roll]
        print("Student record deleted.\n")
    else:
        print("Student not found.\n")

def main():
    while True:
        print("==== Student Management System ====")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            display_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
