class Course:
    def __init__(self):
        self._id= input("Enter the course id:")
        self._name= input("Enter the course name:")
    def get_id(self):
        return self._id
    def get_name(self):
        return self._name
class Utils:
    def input_sth(args):
        return int(input(f"Enter the number of {args}"))
    
class Univercity:
    def __init__(self):
        self._num_of_student=0
        self._num_of_course=0
        self._students=[]
        self._courses=[]
    def get_num_student(self):
        return self._num_of_student
    def get_num_course(self):
        return self._num_of_course
    def get_student(self):
        return self._students
    def get_course(self):
        return self._courses
    def add_course(self):
        course = Course()
        self._courses.append(course)
        self._num_of_course += 1

    def add_student(self):
        student_id = input("Enter the student id: ")
        student_name = input("Enter the student name: ")
        student_dob = input("Enter the student date of birth (dd/mm/yyyy): ")
        self._students.append({"id": student_id, "name": student_name, "dob": student_dob})
        self._num_of_student += 1

    def list_courses(self):
        print("\nList of Courses:")
        for course in self._courses:
            print(f"- ID: {course.get_id()}, Name: {course.get_name()}")

    def list_students(self):
        print("\nList of Students:")
        for student in self._students:
            print(f"- ID: {student['id']}, Name: {student['name']}, DOB: {student['dob']}")


def main():
    university = Univercity()
    print("Welcome to the University Management System")

    while True:
        print("\nOptions:")
        print("1. Add a course")
        print("2. Add a student")
        print("3. List all courses")
        print("4. List all students")
        print("5. Exit")

        choice = int(input("Select an option: "))

        if choice == 1:
            university.add_course()
        elif choice == 2:
            university.add_student()
        elif choice == 3:
            university.list_courses()
        elif choice == 4:
            university.list_students()
        elif choice == 5:
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()