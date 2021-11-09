student_score = input("input a list of student score ").split()
for n in range(0,len(student_score)):
    student_score[n]=int(student_score[n])
print(student_score)
c=int(student_score[0])
for n in student_score:
    if(c<n):
        c=n
print(f"the max val is : {c}")
