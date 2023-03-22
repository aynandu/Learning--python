import re

validation =re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
password= re.compile(r"[a-zA-Z0-9@#_]{8,}[0-9]")
passchecker="Nandu@1234"
gmail_id= "ng@g.com"
z=validation.search(gmail_id)
y=password.fullmatch(passchecker)
print(y)
if validation.search(gmail_id):print(z)
else: print("incorrect email id, Try again")