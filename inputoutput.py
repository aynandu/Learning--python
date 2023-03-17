#Better way to work with files in Python
''''
with open('text.txt',mode='r') as my_file2:
    print(my_file2.read())                 # ()............. read a file ouside
'''
with open('sad.txt',mode='w')as my_file3:
    txt2=my_file3.write("new one")
    print(txt2)   #()..........write also  Create new file

with open('app/newfile.txt',mode='w')as my_file4:
    txt3=my_file4.write("my Name is nandu")
    print(txt3)   #()....................adding a new file to just created folder ..
# NB:  ./app/ means current folder ,  ../app/ means one folder back from current folder

with open('text.txt',mode='r+') as my_file2:
    text= my_file2.write(":)")
    print(text)                 ## ()............. write into a file ouside
# r - read, r+ - read write , w- write,a - append

print('**********(1)************* ')
#-----Input a file and output itself
my_file=open('text.txt')
print(my_file.read())
my_file.seek(0)
print(my_file.read())
my_file.seek(0)
print(my_file.read())           #.............(1)read

print('**********(2)*************')
print(my_file.readline())  #.............(1)readline 


print(my_file.readlines()) #.............(1)readlines

# Not working (2&3)
#my_file.close() #-------------close it  

#...............Excercise..................
from translate import Translator
translator=Translator(to_lang="kor")
try:
    with open('./app/newfile.txt',mode='r') as excer:
        textchanger= excer.read()
        trans=translator.translate(textchanger)
        print(trans)
        with open('./app/newtransilatefile.txt', mode='w') as excer2:
            excer2.write(trans)
except FileNotFoundError as err:
    print("your file path")
