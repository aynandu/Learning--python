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

#*******************************  Decorator Excercise  ***************************************
user1 = {
    'name': 'Sorna',
    'valid': True 
}


def authenticated(fn):
    def verification(use):
      if  user1['valid']:
       return fn(use)
      else:
          print('message can\'t be send')

    return verification     

@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)

#*******************************  Generators Excercise *************************************** 
def special_function(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            print(next(iterator))
        except StopIteration:
            break
special_function([1,2,3])      #Normal Function with Iteration
class MyGenRange():
    current =0
    def __init__(self, first,last):
        self.first = first
        self.last = last
    def __iter__(self):     #iter allows to create iterable ..looping class
        return self
    def __next__(self):
        if MyGenRange.current <self.last:
            num=MyGenRange.current
            MyGenRange.current +=1
            return num
        raise StopIteration
    

gen = MyGenRange(0,100)
                        # Make this work!! creating our on range func using Generators
for i in gen:               
    print(i)

#***********************Excecise 2
def fib(number):
    a = 0
    b = 1
    for i in range(number):
        yield a
        temp =a
        a=b
        b=temp+b

for i in fib(20):
    print(i)                #using Generators  _____1

def fib2(number):
    a = 0
    b = 1
    result = []
    for i in range(number):
        result.append(a)
        temp =a
        a=b
        b=temp+b
    return result

print(fib2(20))             #using List _____2

inp =int(input("value : "))
fact=1                           #n10=n10xn9xn8...n1
for i in range(1,inp+1):
    fact= fact *i
    print(fact)