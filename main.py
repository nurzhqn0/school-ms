from contextlib import nullcontext


class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # Getter for name
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and value.strip() and not any(char.isdigit() for char in value):
            self.__name = value
        else:
            raise ValueError("Name must be a non-empty string and does not contain digits")

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if isinstance(value, int) and value >= 0:
            self.__age = value
        else:
            raise ValueError("Age must be a non-negative or non-empty integer")

    def __str__(self):
        return f"Name: {self.__name}, Age: {self.__age}"


class Student(Person):
    def __init__(self, name, age, student_id, grade):
        super().__init__(name, age)
        self.__student_id = student_id
        self.__grade = grade

    @property
    def student_id(self):
        return self.__student_id

    @student_id.setter
    def student_id(self, value):
        if isinstance(value, int) and value >= 0:
            self.__student_id = value
        else:
            raise ValueError("Student ID must be a non-negative or non-empty integer")

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, value):
        valid_grades = ["A", "B", "C", "D", "F"]
        if isinstance(value, str) and len(value) == 1 and (value.upper() in valid_grades):
            self.__grade = value.upper().strip()

        else:
            raise ValueError("Grade must be one of the following: A, B, C, D, F.")

    def get_details(self):
        return f"{super().__str__()}, Student ID: {self.__student_id}, Grade: {self.__grade}\n"


class Teacher(Person):
    def __init__(self, name, age, teacher_id, subject):
        super().__init__(name, age)
        self.__teacher_id = teacher_id
        self.__subject = subject

    @property
    def teacher_id(self):
        return self.__teacher_id

    @teacher_id.setter
    def teacher_id(self, value):
        if isinstance(value, int) and value >= 0:
            self.__teacher_id = value
        else:
            raise ValueError("Teacher ID must be a non-negative or non-empty integer")

    @property
    def subject(self):
        return self.__subject

    @subject.setter
    def subject(self, value):
        if isinstance(value, str) and value.strip() and not any(char.isdigit() for char in value):
            self.__subject = value

        else:
            raise ValueError("Subject must be a non-empty string")

    def get_details(self):
        return f"{super().__str__()}, Teacher ID: {self.__teacher_id}, Subject: {self.__subject}"

class Classroom:
    def __init__(self, room_number, students, teacher):
        self.__room_number = room_number
        self.__students = students
        self.__teacher = teacher

    @property
    def room_number(self):
        return self.__room_number

    @room_number.setter
    def room_number(self, value):
        if isinstance(value, int) and value >= 0:
            self.__room_number = value

    @property
    def students(self):
        return self.__students

    @students.setter
    def students(self, value):
        if isinstance(value, list) and len(value) > 0 and all(isinstance(student, Student) for student in value):
            self.__students = value

        else:
            raise ValueError("Students must be a non-empty list")

    @property
    def teacher(self):
        return self.__teacher

    def set_teacher(self, value):
        if isinstance(value, Teacher):
            self.__teacher = value
        else:
            raise ValueError("Teacher must be a non-empty Teacher")

    def add_student(self, student: Student):
        if isinstance(student, Student):
            self.__students.append(student)

        else:
            raise ValueError("Student must be a non-empty Student")

    def get_student_list(self):
        print(f"Classroom {self.__room_number}:")
        print(f"Teacher {self.__teacher.name}, Subject: {self.__teacher.subject}")
        for i, student in enumerate(self.__students, 1):
            print(f"{student.name} (ID: {student.student_id}, Grade: {student.grade})")


def display_menu():
    print("Menu:")
    print("1. Add a student")
    print("2. Add a teacher")
    print("3. Create a classroom")
    print("4. Assign teacher to a classroom")
    print("5. Add student to a classroom")
    print("6. Display classroom information")
    print("7. Search for students by grade")
    print("8. Exit")

def main():
    students = []
    teachers = []
    classrooms = []

    try:
        while True:
            display_menu()
            choice = input("\nYour choice: ").strip()

            if choice == "1":
                student = Student(None, None, None, None)
                try:
                    student_name = input("Enter student name: ")
                    student.name = student_name

                    student_age = int(input("Enter age: "))
                    student.age = student_age

                    student_id = int(input("Enter student ID: "))
                    is_exist = any(student.student_id == student_id for student in students)
                    if is_exist:
                        raise ValueError("Student with such ID already exists")
                    student.student_id = student_id

                    student_grade = input("Enter grade: ")
                    student.grade = student_grade

                    students.append(student)
                    print(f'\nStudent "{student.name}" added successfully!\n')
                except Exception as e:
                    print(f"\nError: {e}\n")
            elif choice == "2":
                teacher = Teacher(None, None, None, None)
                try:
                    teacher_name = input("Enter teacher name: ")
                    teacher.name = teacher_name

                    teacher_age = int(input("Enter age: "))
                    teacher.age = teacher_age

                    teacher_id = int(input("Enter teacher ID: "))
                    is_exist = any(teacher.teacher_id == teacher_id for teacher in teachers)
                    if is_exist:
                        raise ValueError("Teacher with such ID already exists")
                    teacher.teacher_id = teacher_id

                    teacher_subject = input("Enter subject: ")
                    teacher.subject = teacher_subject

                    teachers.append(teacher)
                    for teacher in teachers:
                        print(teacher.get_details())
                    print(f'\nTeacher "{teacher.name}" added successfully!\n')
                except Exception as e:
                    print(f"\nError: {e}\n")
            elif choice == "3":
                classroom = Classroom(None, [], None)

                try:
                    classroom_number = int(input("Enter classroom number: "))
                    is_exist = any(classroom.room_number == classroom_number for classroom in classrooms)
                    if is_exist:
                        raise ValueError("Classroom with such number already exists")
                    classroom.room_number = classroom_number

                    classrooms.append(classroom)
                    print(f"\nClassroom {classroom.room_number} was successfully created!\n")
                except Exception as e:
                    print(f"\nError: {e}\n")

            elif choice == "4":
                try:
                    classroom_number = int(input("Enter classroom number: "))

                    teacher_id = int(input("Enter teacher ID to assign: "))
                    found_teacher = next((teacher for teacher in teachers if teacher.teacher_id == teacher_id), None)

                    if not found_teacher:
                        raise ValueError('Teacher with such ID does not exist!')

                    found = False
                    for classroom in classrooms:
                        if classroom.room_number == classroom_number:
                            classroom.set_teacher(found_teacher)
                            found = True
                            break

                    if found:
                        print(f'\nTeacher "{found_teacher.name}" assigned to classroom {classroom_number} successfully!\n')
                    else:
                        raise ValueError(f'Error: Classroom {classroom_number} not found!')
                except Exception as e:
                    print(f"\nError: {e}\n")
            elif choice == "5":
                classroom_number = int(input("Enter classroom number: "))

                student_id = int(input("Enter student ID to assign: "))
                found_student = next((student for student in students if student.student_id == student_id), None)

                if not found_student:
                    raise ValueError('Student with such ID does not exist!')

                found = False
                for classroom in classrooms:
                    if classroom.room_number == classroom_number:
                        classroom.add_student(found_student)
                        found = True
                        break

                if found:
                    print(f'\nStudent "{found_student.name}" assigned to classroom {classroom_number} successfully!\n')
                else:
                    raise ValueError(f'Error: Classroom {classroom_number} not found!')
            #
            # elif choice == "6":
            #
            elif choice == "7":
                print("Thank you for using the Mini School Management System!")
                break
            else:
                print("Invalid option. Please try again.")

    # i want to handle the case when user manually stopped program
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting gracefully.")

if __name__ == "__main__":
    print("Welcome to the Mini School Management System!\n\n")
    main()