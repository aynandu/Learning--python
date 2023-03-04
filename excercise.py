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

#finding square using Lambda
my_list =[5,4,3]

print(list(map(lambda item: item **2 , my_list)))

#finding List sorting using lambda
a=[(0,2),(4,3),(10,-1),(9,9)]
a.sort(key=lambda x:x[1])
print (a)