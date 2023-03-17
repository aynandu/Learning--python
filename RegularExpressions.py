#Regular Expressions is used to validation ,search , check a piece or a group of string. eg : for email & Password checking for verification.
import re

pattern=re.compile('this')
string="search this inside of this string"
a=pattern.search(string)
print(a.span())
print(a.start())
print(a.group())            #group is useful when you do multiple search of single word.


b=pattern.findall(string)           #disply all the strings you search for
c=pattern.fullmatch(string)         #check both full strings are equal
d=pattern.match(string)             #Display only strings upto match index
print(b)

#................Email Validation.... regular expression

validation =re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
password= re.compile(r"[a-zA-Z0-9@#_]{8,}[0-9]")
passchecker="Nandu@1234"
gmail_id= "ng@g.com"
z=validation.search(gmail_id)
y=password.fullmatch(passchecker)
print(y)
if validation.search(gmail_id):print(z)
else: print("incorrect email id, Try again")

