students = []

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        roll = int(input("Enter Roll No: "))
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        course = input("Enter Course: ")
        marks = float(input("Enter Marks: "))

        student = {
            "Roll No": roll,
            "Name": name,
            "Age": age,
            "Course": course,
            "Marks": marks
        }

        students.append(student)
        print("Student added successfully!")

    elif choice == 2:
        print("\n--- Student Records ---")
        for s in students:
            print(
                s["Roll No"],
                s["Name"],
                s["Age"],
                s["Course"],
                s["Marks"]
            )

    elif choice == 3:
        roll = int(input("Enter Roll No to search: "))

        found = False
        for s in students:
            if s["Roll No"] == roll:
                print("\nStudent Found:")
                print(s)
                found = True
                break

        if not found:
            print("Student not found!")

    elif choice == 4:
        roll = int(input("Enter Roll No to delete: "))

        for s in students:
            if s["Roll No"] == roll:
                students.remove(s)
                print("Student deleted successfully!")
                break
        else:
            print("Student not found!")

    elif choice == 5:
        print("Program ended.")
        break

    else:
        print("Invalid choice!")