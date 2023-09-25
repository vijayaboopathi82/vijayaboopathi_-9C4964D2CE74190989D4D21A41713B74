class Student:
    def __init__(self,name,roll_number,cgpa):
        self.name=name
        self.roll_number=roll_number
        self.cgpa=cgpa
def sort_students(student_list):
    sorted_students=sorted(student_list,key=lambda student:student.cgpa,reverse=True)
    return sorted_students
student1= Student("Priya","S123",9.2)
student2= Student("Vijay","S124",8.9)
students=[student1,student2]
sorted_students=sort_students(students)
for student in sorted_students:
    print("Name:{student.name},Roll Number:{student.roll_number},CGPA:{student.cgpa}")
        
