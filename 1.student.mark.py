def input_number_of_students():
    return int(input("Enter the number of students in the class: "))

def input_students():
    students = []
    num_students = input_number_of_students()
    for _ in range(num_students):
        student_id = input("Enter student id: ")
        student_name = input("Enter student name: ")
        student_dob = input("Enter student date of birth (dd/mm/yyyy): ")
        students.append({"id": student_id, "name": student_name, "dob": student_dob})
    return students

def input_number_of_courses():
    return int(input("Enter the number of courses: "))

def input_courses():
    courses = []
    num_courses = input_number_of_courses()
    for _ in range(num_courses):
        course_id = input("Enter the course id: ")
        course_name = input("Enter the course name: ")
        courses.append({"id": course_id, "name": course_name})
    return courses

def input_marks(students, courses):
    marks = {}
    for course in courses:
        course_id = course['id']
        print(f"\nEntering marks for course: {course['name']} ({course_id})")
        marks[course_id] = {}
        for student in students:
            mark = float(input(f"Enter mark for {student['name']} ({student['id']}): "))
            marks[course_id][student['id']] = mark
    return marks

def list_courses(courses):
    print("\nList of Courses:")
    for course in courses:
        print(f"- ID: {course['id']}, Name: {course['name']}")

def list_students(students):
    print("\nList of Students:")
    for student in students:
        print(f"- ID: {student['id']}, Name: {student['name']}, DOB: {student['dob']}")

def show_marks(students, courses, marks):
    print("\nAvailable courses:")
    for i, course in enumerate(courses):
        print(f"{i + 1}. {course['name']} ({course['id']})")
    
    course_index = int(input("Select a course by number: ")) - 1
    selected_course = courses[course_index]
    course_id = selected_course['id']

    print(f"\nMarks for course: {selected_course['name']} ({course_id})")
    for student in students:
        mark = marks[course_id].get(student['id'], "N/A")
        print(f"- {student['name']} ({student['id']}): {mark}")

def main():
    print("Welcome to the Student Management System")

    students = input_students()
    courses = input_courses()
    marks = input_marks(students, courses)

    while True:
        print("\nOptions:")
        print("1. List all courses")
        print("2. List all students")
        print("3. Show student marks for a course")
        print("4. Exit")

        choice = int(input("Select an option: "))

        if choice == 1:
            list_courses(courses)
        elif choice == 2:
            list_students(students)
        elif choice == 3:
            show_marks(students, courses, marks)
        elif choice == 4:
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

