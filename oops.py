#OOPs
#Class
class PlayerDetails:
    membership = True #Class Object Attributes
    def __init__(self,name , age):
       self.name =name # attribbutes
       self.age=age
    def Shout(self):
        print(f'my name {self.name}')
        

player1=PlayerDetails("Nandu",27)
player2=PlayerDetails("Reshmi",26)

print(player1.name , player1.age)
print(player2.name , player2 .age)
print(player1.Shout())
# Create Class for finding out oldest cast excercise
class cat:
    species = 'mamals'
    def __init__(self,name,age):
        self.name = name
        self.age=age
       
# 1 Instantiate the Cat object with 3 cats
tobby=cat('tobby',1)
marry=cat('marry',6)
labby=cat('labby',9)
# 2 Create a function that finds the oldest cat
def getmaxagecat(*arg):
    return max(arg)
# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f'Oldest cat will have  {getmaxagecat(tobby.age,marry.age,labby.age)} years old')

#without class

petty = ('petty',1)
titty=('titty',4)
mitty=('mitty',8)
print(f'Oldest cat will have  {getmaxagecat(petty[1],titty[1],mitty[1])} years old')
#Excercise 2
class Pets():
    animals = []
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'

#1 Add nother Cat
class tobby(Cat):
    def sing(self,sounds):
        return f'{sounds}'

#2 Create a list of all of the pets (create 3 cat instances from the above)
my_cats = [Simon('Simon',4),Sally('Sally',6),tobby('tobby',7)]
#3 Instantiate the Pet class with all your cats use variable my_pets
my_pet = Pets(my_cats)
#4 Output all of the cats walking using the my_pets instance
my_pet.walk()
#Inherintance in class...
class user():
    def __init__(self,email):
        self.email=email
        
    def sign_in(self):
        print("you are logged in")
        print(f'email :  {self.email}')

class wizard(user):
    def __init__(self,name,power ):
        #super().__init__(email)  ... super class method...
        self.name =name
        self.power=power
    def attack(self):
        print(f' wizard {self.name} having a power of {self.power}')

class archer(user):
     def __init__(self,name,arrows):
        self.name =name
        self.arrows=arrows
     def attack(self):
        print(f' Archer {self.name} having a arrows left is {self.arrows}')
     def run(self):
        print('run  really fast')

class HybridBorg(wizard,archer):
   def __init__(self, name, power, arrows):
       archer.__init__(self,name,arrows)
       wizard.__init__(self,name,power)


wizard1=wizard('Fireball',50,)
archer1=archer('Archi',100)
wizard1.attack()
archer1.attack()

#print(dir(wizard1)) # intersection - displys what are the function &methods can accessable during run.
hb1=HybridBorg('Borg',50,100,)
print(hb1.attack())


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
my_list = [1,2,3]
your_list=(10,20,30)
print(list(zip(my_list,your_list))) #Using Zip

from functools import reduce    # Using reducer
def accumilator(acc , item):
    print(acc , item)
    return acc + item

print(reduce(accumilator,my_list,0))
#*******************************  LAMBDA  ***************************************
print("lambda function (by map):  ",list(map(lambda item : item*2 , my_list)))
print("lambda function (by filter):  ",list(filter(lambda item : item%2!=0 , my_list)))
print("lambda function (by reducer):  ",reduce(lambda acce, item:acce+item, my_list))
#*******************************  LAMBDA  ***************************************
my_petname = ['tobby','marco','tunny']
 
def Capitilize(items):
    return items.upper()

print('Map : ',list(map(Capitilize,my_petname))) 

my_string = ['a','b','c','d']
my_numbers = [5,4,3,2]

print(list(zip(my_string,sorted(my_numbers))))
scores = [73, 20, 65, 19, 76, 100, 88,50]
def mark_Scored(items):
    return items>50

print(list(filter(mark_Scored,scores)))