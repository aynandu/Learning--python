#Username &Password Excercise
#userName=input('Username : ')
#userPassword=input('Password: ')
#lengthPassword=len(userPassword)
#hiddenPassword='*'*lengthPassword
#print(f"hi{userName} your password {hiddenPassword} is {lengthPassword} Letter's long")

picture = [
[0,0,0,1,0,0,0],
[0,0,1,1,1,0,0],
[1,1,1,1,1,1,1],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0]
]
for item in picture:
    for pixcel in item:
        if (pixcel):
            print('*', end='')
        else:
                print(' ', end='')
    print('')
some_list = ['a','b','c','b','d','m','n','n']
duplicate = []
for value in some_list:
    if some_list.count(value)>1:
        if value not in duplicate:
          duplicate.append(value)
print (duplicate)
class SuperList(list):
    def __len__(self):
        return 1000

super_list1=SuperList()
print(len(super_list1))
super_list1.append(5)
print(super_list1[0])
print(issubclass(SuperList,list))

def Multiply_by2(l1): #Pure Function
    multipl_number=[]
    for item in l1:
        multipl_number.append(item*2)
    return multipl_number

print(Multiply_by2([1,2,3]))

#or
def Addition_2(item): 
    return item*2
print(list(map(Addition_2,[1,2,3]))) #Using Map 

def odd_output (item):
    return item %2 !=0

print(list(filter(odd_output,[1,2,3]))) #Using Filter