def student_data():
    student = []
        
    no = int(input("\n Enter The No Of Student : "))

    if no < 5:
        print("Give 5 Or More Student Only")
    else:
        for i in range(no):
            name = input("Enter The student_name : ")
            sub1 = int(input("Enter The Subject1 Marks : "))
            sub2 = int(input("Enter The Subject2 Marks : "))
            sub3 = int(input("Enter The Subject3 Marks : "))
            sub4 = int(input("Enter The Subject4 Marks : "))
            sub5 = int(input("Enter The Subject5 Marks : "))
            
            if ((sub1 >=0 and sub1<=100) and (sub2 >=0 and sub2<=100) and (sub3>=0 and sub3<=100) and (sub4>=0 and sub4<=100) and (sub5>=0 and sub5<=100)):
                student.append([name,sub1,sub2,sub3,sub4,sub5])
            else:
                print("Invalid Marks! Please Enter Marks Between 0 And 100.")
                return None

    return student
        

def student_data_total_and_per(student):
    # total_marks = []
    for stud in student:
            total = stud[1] + stud[2] + stud[3] + stud[4] + stud[5]
            per = total / 5.0
            # total_marks.append({
            # "name": stud[0],
            # "total_mrk": total
            # })
            stud.append(total)
            stud.append(per)
    # return total_marks
    return student

def student_record_grade(student):
    for stud in student:
            if stud[1]>40 and stud[2]>40 and stud[3]>40 and stud[4]>40 and stud[5]>40:

                if stud[7] >= 90 and stud[7] <= 100:
                    grade = 'A'
                elif stud[7] >= 80 and stud[7] < 90:
                    grade = 'B'
                elif stud[7] >= 70 and stud[7] < 80:
                    grade = 'C'
                elif stud[7] >= 60 and stud[7] < 70:
                    grade = 'D'
                elif stud[7] >= 50 and stud[7] < 60:
                    grade = 'E'
                elif stud[7] >= 41 and stud[7] < 50:
                    grade = 'F'
                else:
                    grade = 'Fail'
            else:
                grade = '-'
                stud[7] = 0.0
                
            stud.append(grade)
        
    return student    

def student_processed_record(student):
    total_and_per = student_data_total_and_per(student)
    processed_record = student_record_grade(student)
    return processed_record