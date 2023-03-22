#IF - elif - else : Condition 
is_Old = True
is_License=False

if is_Old and is_License:
    print('you are old enought to drive')
elif is_Old and not is_License: 
    print('you dont have  license')
else:
    print('you are not old enough to drive')

#Ternary Operation : Condition_if_True if Condition else Condition_if_False
twitter_friend = True
Can_message='Message allowed' if twitter_friend else 'message not allowed'
print(Can_message)
#SHORT cIRCUTING..
if is_Old or is_License:
    print('you can drive')
print ('********end of if statemnet**********')
my_mark = [10,20,30,40,50]
slno =0
for subject in my_mark:
    slno+=1
    print(f'subject {slno} is {subject}')
print ('********end of for statemnet**********')
runner = 0
while runner <2:
    runner=runner+1
    print(f" passess {runner} Km Now")
while True:
    response=input("say something : ")
    if response == "by":
        break
print ('********end of while statemnet**********')
print ('********Functionst**********')
#parametes
def say_hello(name,age):
    print(f'hello {name},you are {age} years of old')
#arguments
say_hello('Nandu',27) #call or invoking
#Nested Function & Return Fuctions
def class_X(mark1,mark2):
    def mark_students(m1,m2):
       return m1+m2
    return mark_students(mark1,mark2)
total_marks = class_X(90,90)
print(total_marks)

def highest_even (argeven):
    total_even = []
    for value in argeven:
      if value %2==0:
        total_even.append(value)
    return max(total_even)
    
print (highest_even([10,2,3,4,8,11]))
# Walrus operator - large equation is assisgn to a variable
Letter = 'Nanduuuuu'
if ((n:=len(Letter))>4):
    print(f'letter having {n} words')
def outer():
    x="local"
    
    def inner():
        nonlocal x
        x = "non local"
        
        print('inner : ' +x)
    inner()

    print('outer: ' +x)
outer()
