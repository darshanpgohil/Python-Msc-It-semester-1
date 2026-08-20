from student_record import student_data
from student_record import student_processed_record
from ranking import return_ranks_of_student
from report import print_data

student = student_data()
if student:
    processed_record = student_processed_record(student)
    rank = return_ranks_of_student(processed_record)

    print_data(rank)