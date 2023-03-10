#********Error Handling >>>*************Try - Except - Else ************** 
""" 
while True:
    try:
        age = int(input("Enter Your Age : "))
        10/age
        print(age)
    except ValueError:
        print("Please Enter a number ")
    except ZeroDivisionError:
        print("Please enter a number Other than 0")
    else:
        print("Thankyou") 
        break
    finally:
        print("ok done") 
"""
 #break function not working!
def sum(num1, num2):
    try:
        return num1/num2
    except (TypeError,ZeroDivisionError) as err:
        print(err)

print(sum(1,0))
print(sum(1,'2'))

while True:
    try:
        age = int(input("Enter Your Age : "))
        10/age
        raise ValueError('Hey cut it out')  # creating a Error.. 
    except ZeroDivisionError:
        print("Please enter a number Other than 0")
