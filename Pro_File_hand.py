while True:

    print("\n===== Student Marks Notebook =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Exit")
    print("5. Clear All Students")

    choice = input("Enter your choice: ")

    # 1. Add Student
    if choice == "1":

        name = input("Enter student name: ")
        marks = input("Enter marks: ")

        file = open("students.txt", "a")

        file.write(name + " - " + marks + "\n")

        file.close()

        print("Student added successfully")

    # 2. View All Students
    elif choice == "2":

        try:
            file = open("students.txt", "r")

            students = file.readlines()

            if len(students) == 0:
                print("No student records found.")
            else:
                print("\n===== All Students =====")

                for student in students:
                    print(student, end="")

            file.close()

        except FileNotFoundError:
            print("No student records found.")

    # 3. Search Student
    elif choice == "3":

        search_name = input("Enter student name to search: ")

        try:
            file = open("students.txt", "r")

            students = file.readlines()

            found = False

            for student in students:

                if search_name.lower() in student.lower():
                    print("Student found:", student, end="")
                    found = True

            if found == False:
                print("Student not found.")

            file.close()

        except FileNotFoundError:
            print("No student records found.")

    # 4. Exit
    elif choice == "4":

        print("Thank you for using Student Marks Notebook!")
        break
     # 5. Clear All Students
    elif choice == "5":

        try:
            confirm = input(
                "Are you sure you want to delete all students? (yes/no): "
            )

            if confirm.lower() == "yes":

                file = open("students.txt", "w")

                file.close()

                print("All student records have been cleared.")

            else:
                print("Clear operation cancelled.")

        except FileNotFoundError:
            print("No student records found.")

    # Invalid Choice
    else:

        print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")
