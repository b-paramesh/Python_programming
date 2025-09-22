'''write a program to Enter student number,student name,3 subjects marks and find total,average of students print all tudent details'''
studentNumber=int(input("Enter the student number:"))
studentName=input("Enter the student name:")
studentMarks1=int(input("Enter the student marks subject 1:"))
studentMark2=int(input("Enter the student marks subject 2:"))
studentMark3=int(input("Enter the student marks su25bejct 3:"))
total=studentMarks1+studentMark2+studentMark3
average=round(total/3,2)
print("studentNumber",studentNumber,"studentName",studentName,"\nstudentMarks1 ",studentMarks1,
      "\nstudentName2 ",studentMark2,"\nstudentMarks3 ",studentMark3,"\ntotal:",total,"\naverage:",average)