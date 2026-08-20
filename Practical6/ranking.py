def student_sort(student):
    student.sort(key=lambda x:x[7],reverse=True)
    return student

def assign_ranks(student):

    rank = 1
        
    for record in range(len(student)):
        if record == 0:
            student[record].append(rank)
        elif student[record][7] == student[record-1][7]:
            student[record].append(rank)
        else:
            rank = record + 1
            student[record].append(rank)
                
    return student

def ranks_student(student):
    sorted_student = student_sort(student)
    student_rank = assign_ranks(sorted_student)
    
    return student_rank

def return_ranks_of_student(student):
    ranking = ranks_student(student)
    return ranking    