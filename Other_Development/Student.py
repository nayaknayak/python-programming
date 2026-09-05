from FunctionsInPython import greet

class Student:
   name = 'satya'
   id =101
   def students_detaails(self):
        greet(self.name)
        print(" Name is ", self.name, " id is " ,Student.id)
            
s1= Student()
s1.students_detaails()
