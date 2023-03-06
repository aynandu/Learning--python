#*******************************  LAMBDA  ***************************************
from functools import reduce 
my_list = [1,2,3]
print("lambda function (by map):  ",list(map(lambda item : item*2 , my_list)))
print("lambda function (by filter):  ",list(filter(lambda item : item%2!=0 , my_list)))
print("lambda function (by reducer):  ",reduce(lambda acce, item:acce+item, my_list))
#*******************************  List / set / Dictionary Comprehension ()/{}/{:} ***************************************
my_data_list=[char for char in 'hello']
my_data_list2 =[num for  num in range(0,100)]
my_data_list3=(num**2 for num in range (0,100))
my_data_list4 = [num**2 for num in range (0,100) if num %2==0]

print('\nList Comprehension (Character): ',my_data_list)
print('\nList Comprehension (range): ',my_data_list2)
print('\nList Comprehension (square root): ',my_data_list3)
print('\nList Comprehension(even from square root): ',my_data_list4)

simple_dict={
    'a':1,
    'b':2
}
my_dict={key : value*2 for key,value in simple_dict.items() if value %2==0}
print('\nDict Comprehension(only even): ',my_dict)  # Dict Comprehension

my_dict2= {value : value*2 for value in [1,2,3]}  # Dict Comprehension
print('\nDict Comprehension: ',my_dict2)
#*******************************  Decorators *************************************** using fuctions as verables/ parameter for other functions. 
# high order functions - a function can accept or return or both another  function
def my_decorators(func):
    def wrap_func():
        print("********************")
        func()
        print("********************")
    return wrap_func

@my_decorators
def hello():
    print('helloooo')   #************************ (1) Using Decorator

def hey():
    print('heyyyy')     #************************ (2) Normal Function

hello()                 #************************ (1) Using Decorator 
hey2=my_decorators(hey)   
hey2()                  #************************ (2)  Normal Function 
#wrapping Normal function with Decorator how simple is that! Decorator's are doing (2)

def my_decor(func):
    def  calling_details(x):
        print("**********************")
        func(x)
        print("**********************")
    return calling_details

@my_decor
def details(det):
    print(det)
details('hi helloo')

from time import time
def performance(func):
    def wrap_perfor():
        time1= time()
        result=func()
        time2=time()
        print(f'time look {time2 - time1} ms')
        return result
    return wrap_perfor

@performance
def long_time():
    for i in range(10000000):
        i*5

long_time()
        
#*******************************  Excercise  ***************************************
some_list=['a','n','c','n','d','m','b','b']

duplicates=list(set([items for items in some_list if some_list.count(items)>1]))
print("\nExcercise : " , duplicates)

setter = set(['q','q','a','a','a','d','d'])
print(list(setter)) 
