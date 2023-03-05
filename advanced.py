#*******************************  LAMBDA  ***************************************
from functools import reduce 
my_list = [1,2,3]
print("lambda function (by map):  ",list(map(lambda item : item*2 , my_list)))
print("lambda function (by filter):  ",list(filter(lambda item : item%2!=0 , my_list)))
print("lambda function (by reducer):  ",reduce(lambda acce, item:acce+item, my_list))
#*******************************  List Comprehension  ***************************************
my_data_list=[char for char in 'hello']
my_data_list2 =[num for  num in range(0,100)]
my_data_list3=[num**2 for num in range (0,100)]
my_data_list4 = [num**2 for num in range (0,100) if num %2==0]

print('\nList Comprehension (Character): ',my_data_list)
print('\nList Comprehension (range): ',my_data_list2)
print('\nList Comprehension (square root): ',my_data_list3)
print('\nList Comprehension(even from square root): ',my_data_list4)