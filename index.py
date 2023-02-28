longString ='''
AskingName = input('who r u ')
print('hi '+AskingName) 
'''
print(longString)
InputInteger=6.3
#print(type(InputInteger))
#print(2 ** 6)
#print(9 // 3)  #Answer on top
#print(9  %  3) #Reminder 

#print(bin(8))
print(bin(6))
print(int('0b110', 2))
#type conversion.....
print(type(int(str(100))))
#or
a=str(100)
b=int(a)
c=type(b)
print(c)
#Augmented Operations..
PlanB=10
PlanB +=5
print(PlanB)
#Escape sequences ....
weather = "Hey,it's Sunny \"OOps I forgot Something\"\n happy holiday's"
print(weather)
#Formatted Strings...
userName = 'john luther'
userAge = 55
print(f'hi {userName} your are {userAge}')
#String Index.. slicing
selFish='01234567'
        #01234567
#[start:stop:stepover]
print(selFish[0:7:2])
#bult in function, methods..
print(userName.upper())
print(userName.find('l'))
print(userName.replace('john','Nandu'))
print(userName) #strings are immutable, they can't be changed.
print(len(userName))
#birthYear=input('which year you born: ')
#print(type(birthYear))
#birthYear=2023 - int(birthYear)
#print(f'your age = {birthYear}')
#List Slicing ...
amazon_cart=['laptop',
'Mobile',
'TV',
'Fridge']
print(amazon_cart)
new_cart=amazon_cart[0:3:2]
print(new_cart)
new_cart[0]='car'
print(new_cart)#modifying the list..
new_cart=amazon_cart
new_cart[0]='gum'
print(amazon_cart) # Copying the list
#Matrix
matrix=[
    [1,5,1],
    [0,1,0],
    [1,0,1],
]
print(matrix[0][1]) # in python we use the tern List..
#Listing Method
basket=[1,2,'v',3,5]
#Adding...
basket.append(100)
print(basket)
basket.insert(1,101)
print(basket)
basket.extend([102])
print(basket)
#removing...
basket.pop(0)
print(basket)
basket.remove(101)
print(basket)
#basket.clear()
#print(basket)
print(basket.index(3,0,5))
print('v' in basket)
print('N' in 'im Nandu')
print(basket.count('v'))
basket[1]=1 #Sort & Reverse...
#basket.sort() # This Change Main Data
print(sorted(basket))#This Modifies and create a copy of data
print(basket)
basket.reverse()
print(basket)
sentence=';'
new_sentence=sentence.join(['hi','my','name','is','what']) #new_sentence=';'.join(['hi','my','name','is','what'])
print(new_sentence)
my_tuple=(1,2,3,4) #tuples are imutable. values can't be changable
print(my_tuple[1])
x,y,z, *other=(1,2,0,3,4,5)
print(x,other)
my_set={1,2.3,4,5,5} #set function...
print(my_set)