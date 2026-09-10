#list and tuple 

student = ['John', 'Jane', 'Jack', 'Jill']
print("These are the students:" + str(student))

student_tuple = ('John', 'Jane', 'Jack', 'Jill')
print("These are the students in tuple:" + str(student_tuple))

print("The addition of a new student to the list:")
student.append('Husnain')
print("These are the students after addition:" + str(student))

print("The addition of a new student to the tuple:")
student_tuple += ('Ali',)
print("These are the students in tuple after addition:" + str(student_tuple))