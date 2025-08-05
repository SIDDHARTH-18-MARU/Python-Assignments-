marks = int(input("Enter the marks (0 to 100):"))
if 0 <= marks <= 100:
    if marks>=90:
        Grade = 'A'
    else:
        if marks>=80:
            Grade = 'B'
        else:
            if marks>=70:
                Grade = 'C'
            else:
                if marks>=60:
                    Grade = 'D'
                else:
                    if marks>=50:
                        Grade = 'E'
                    else:
                        Grade = 'F'
    print("Letter Grade:",Grade)
else:
    print("Enter valid marks.")



                        