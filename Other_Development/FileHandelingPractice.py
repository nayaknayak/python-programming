"""
with open("D:/courses.txt","w") as file:
 file.write("104-c#\n")
 file.write("101-java\n")
 file.write("102-python\n")
 file.write("103-Nodejs")

with open("D:/courses.txt","a") as file:
    file.write("\n105-Angular\n")

"""
import os
if os.path.exists("D:/courses.txt"):
    with open("D:/courses.txt","r") as file:
        for line in file:
            print(line)
    with open("D:/courses.txt","w") as file:
        file.write("101- no callses")
         
else:
    print("file not found")