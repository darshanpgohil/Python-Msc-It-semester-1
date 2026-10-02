class Course:
    def __init__(self, course_code,day, start_time, end_time):
        self.course_code = course_code
        self.day = day
        self.start_time = start_time
        self.end_time = end_time

    def __str__(self):
        return self.course_code + "-" + self.day + "-" + self.start_time + "-" + self.end_time

class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def __str__(self):
        result = str(self.student_id) + "\n" 
        result += self.student_name + "\n"

        for course in self.courses:
            result += str(course) + "\n"

        return result

    def check_conflict(self):
        conflict = False

        for i in range(len(self.courses)):
            for j in range(i+1,len(self.courses)):
                c1 = self.courses[i]
                c2 = self.courses[j]

                if c1.day == c2.day:
                    if c1.start_time < c2.end_time and c2.start_time < c1.end_time:
                        print("Conflict " + c1.course_code + " and " + c2.course_code)
                        conflict = True
        
        return conflict

try:
    n = int(input("Enter Number Of Students : "))

    students = []

    for i in range(n):
        print(f"Enter The Student : {i+1}")

        student_id = input("Enter Student Id : ")
        student_name = input("Enter Student Name : ")

        student = Student(student_id, student_name)

        course_count = int(input("Enter Number Of Courses : "))

        for j in range(course_count):
            course_code = input("Enter Course Code : ")            
            day = input("Enter Day : ")
            start_time = input("Enter Start Time (HH:MM): ")
            end_time = input("Enter End Time (HH:MM) : ")

            start = start_time.split(":")
            end = end_time.split(":")

            start_minute = int(start[0]) * 60 + int(start[1])
            end_minute = int(end[0]) * 60 + int(end[1])

            if start_minute >= end_minute:
                raise ValueError("End Time Must Be Greater Than Start Time")

            course = Course(course_code, day, start_time, end_time)

            student.add_course(course)

        students.append(student)

    for student in students:
        print("\n ====================================\n")
        
        print("Total Registered Courses : " + str(len(student.courses)))

        print("\n Checking For Conflicts : ")

        conflict = student.check_conflict()

        if conflict == False:
            print("No Conflicts Found")
            print("Time Table is Valid")
            print(student)

except ValueError as e:
        print("Error : " + str(e))
except Exception as e:
        print("Something went wrong : " + str(e))