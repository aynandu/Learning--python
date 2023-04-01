#send a Spam Mail (included HTML) to any Gmail ID using Python
import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html=Template(Path('index.html').read_text())

email = EmailMessage() #now email become the object
email['Subject'] = 'You won 1,00,0000 dollars!'
email['From'] = 'developerdemo@zohomail.in'
email['To'] = 'nandukannanmala@hotmail.com'
email.set_content(html.substitute({'name':'Nandu','m':'Mr.'}),'html')

with smtplib.SMTP('smtp.zoho.in', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('developerdemo@zohomail.in', 'Developer@1015')
    smtp.send_message(email)
    print("all good boss")