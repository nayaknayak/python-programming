"""
# Reverse a String
name = "Satyabrat Nayak"
nameList=list(reversed(name))
name=""
for i in nameList:
    name= name + i

print(name)

#  Check Given String is palindrome or not
entryNumber= input("Enter a Number to check is it palendrom or not ?  ")
numberstr = entryNumber
numberlist= list(reversed(numberstr))
print(numberlist)
revNumberstr= ""
#for i in numberlist:
 #  revNumberstr= revNumberstr + i

revNumberstr ="".join(numberlist)
if (numberstr == revNumberstr) :
 print("Palendrom")
else:
    print('not a palendrom')




#Count vowels and consonants in string
name = "Satyabrat Nayak"
name=name.upper()
nameLength = len(name)
vowel = ['A','E','I','O','U','E']
for i in range (nameLength):
    nameChar=name[i]
    if nameChar in vowel :
        print("Vowel")
    else:
        print("consultant")

#Count occurence of each character in given string
given_String= "aewwwii"

str_dict= {}
duplecate_char= {}

string_len= len(given_String)
j=2
for i in range (string_len):
    if given_String[i] in str_dict:
        duplecate_char[given_String[i]]=j
        j=j+1
    else:
       str_dict[given_String[i]]=i
   
print(duplecate_char)

 """
#Remove Duplicate Characters in String
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
    



       
