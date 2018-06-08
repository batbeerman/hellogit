#Student dictionary
rec = int(input("Enter no of students :"))
student_dict = {}
for i in range(rec):
        name = input("Enter Student's name :").split()
        marks = input("Enter marks :").split()
        name_key = name[0]
        marks_value = marks[0]
        student_dict[name_key] = {marks_value}
print(student_dict)


#Sorting the above dict
print(sorted(student_dict, key=student_dict.get))


