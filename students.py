# initial declaration
print("How many students do you have?")
numberOfStudents = input()
student_dict = []

for x in range(int(numberOfStudents)):
    entry = {}

    #! input name
    print("Input name of student")
    studentName = input()

    #! input grade
    print("Enter grade(in numeric value)")
    studentGrade = input()

    #! class info
    print("Choose student\'s class")
    print("1--Band 2--Art 3--Science 4--Choir")
    studentClassChoice = input()
    if int(studentClassChoice) == 1:
        studentClass = "Band"
    if int(studentClassChoice) == 2:
        studentClass = "Art"
    if int(studentClassChoice) == 3:
        studentClass = "Science"
    if int(studentClassChoice) == 4:
        studentClass = "Choir"

    #! append dictionary
    entry["Name"] = studentName
    entry["Grade"] = studentGrade
    entry["Class"] = studentClass
    student_dict.append(entry)

for x in student_dict:
    print("Name:", x["Name"]+",", "Grade:",
        x["Grade"]+",", "Class:", x["Class"])