student = []

sub1 = 0
sub2 = 0
sub3 = 0
sub4 = 0
sub5 = 0


no = int(input("\n Enter The No Of Student : "))

i = 0

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
             total = sub1 + sub2 + sub3 + sub4 + sub5
        else:
         print("Invalid Marks! Please Enter Marks Between 0 And 100.")
         break
        
        if sub1>40 and sub2>40 and sub3>40 and sub4>40 and sub5>40:

          per = total / 5.0

          if per >= 90 and per <= 100:
               grade = 'A'
          elif per >= 80 and per < 90:
               grade = 'B'
          elif per >= 70 and per < 80:
               grade = 'C'
          elif per >= 60 and per < 70:
               grade = 'D'
          elif per >= 50 and per < 60:
               grade = 'E'
          elif per >= 41 and per < 50:
               grade = 'F'
          else:
               grade = 'Fail'
        else:
             grade = '-'
             per = 0.0
             rank = '-'

        student.append([name,sub1,sub2,sub3,sub4,sub5,total,per,grade])
     
    sorted =student.sort(key=lambda x:x[7],reverse=True)

    rank = 1
        
    for record in range(len(student)):
        # print(record)
        # if record[7] == student[0][7]:
        #     record.append(rank)
        #     print(record[7])
        #     print(student[0][7])
        # else:
        #     record.append(rank)
        #     rank = rank + 1
        
        if record == 0:
            student[record].append(rank)
        elif student[record][7] == student[record-1][7]:
            student[record].append(rank)
        else:
            rank = record + 1
            student[record].append(rank)

    print(f"{"Name":<10}{"Sub1":<10}{"Sub2":<13}{"Sub3":<10}{"Sub4":<10}{"Sub5":<10}{"Total":<14}{"Per":<11}{"Grade":<10} {"Rank":<10}")

    for student_reco in student:
        print(f"{student_reco[0]:<10} {student_reco[1]:<10} {student_reco[2]:<10} {student_reco[3]:<10} {student_reco[4]:<10} {student_reco[5]:<10} {student_reco[6]:<10} {student_reco[7]:<10} {student_reco[8]:<10} {student_reco[9]:<10}")