class classOfStudents:
    def __init__(self):
        print('constructor of parent')
    def student_village(self,village_name: str):
        print(f"name define in student class is {village_name}")
        
class student(classOfStudents):
    def student_name(self, name):
      #  super().student_name('mama')
        print(f"name define in student class is {name}")
        
s1=student()
s1.student_village('jajpur')
s1.student_name('mama')
        


    