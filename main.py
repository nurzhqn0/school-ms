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
            raise ValueError("\nName must be a non-empty string")

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if isinstance(value, int) and value >= 0:
            self.__age = value
        else:
            raise ValueError("\nAge must be a non-negative or non-empty integer")

    def __str__(self):
        return f"Name: {self.__name}, Age: {self.__age}"


class Student(Person):
    def __init__(self, name, age, student_id, grade):
        super().__init__(name, age)
        self._student_id = student_id
        self.__grade = grade

    @property
    def student_id(self):
        return self._student_id

    @student_id.setter
    def student_id(self, value):
        if isinstance(value, int) and value >= 0:
            self._student_id = value
        else:
            raise ValueError("\nStudent ID must be a non-negative or non-empty integer")

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
        return f"{super().__str__()}, Student ID: {self._student_id}, Grade: {self.__grade}"


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
            raise ValueError("\nTeacher ID must be a non-negative or non-empty integer")

    @property
    def subject(self):
        return self.__subject

    @subject.setter
    def subject(self, value):
        if isinstance(value, str) and value.strip() and not any(char.isdigit() for char in value):
            self.__subject = value

        else:
            raise ValueError("\nSubject must be a non-empty string")

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
            raise ValueError("\nStudents must be a non-empty list")

    @property
    def teacher(self):
        return self.__teacher

    @teacher.setter
    def teacher(self, value):
        if isinstance(value, Teacher):
            self.__teacher = value
        else:
            raise ValueError("\nTeachers must be a non-empty list")
