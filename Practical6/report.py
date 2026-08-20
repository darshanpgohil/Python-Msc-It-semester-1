def print_data(student):
        print(f"{"Name":<10}{"Sub1":<10}{"Sub2":<13}{"Sub3":<10}{"Sub4":<10}{"Sub5":<10}{"Total":<14}{"Per":<11}{"Grade":<10} {"Rank":<10}")

        for student_reco in student:
            print(f"{student_reco[0]:<10} {student_reco[1]:<10} {student_reco[2]:<10} {student_reco[3]:<10} {student_reco[4]:<10} {student_reco[5]:<10} {student_reco[6]:<10} {student_reco[7]:<10} {student_reco[8]:<10} {student_reco[9]:<10}")