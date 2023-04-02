#get a password and check wheather it safe or not.


import requests             #allow as to make a request
import hashlib              #use to generate sha1password
import sys
import pathlib

def request_api_data(query_char):
    url="http://api.pwnedpasswords.com/range/"+query_char
    res=requests.get(url)
    if res.status_code !=200:
        raise RuntimeError(f'Error featching: {res.status_code},check api and try again')
    return res

def get_password_leak_count(hashes,hashe_to_check):
    #print (hashes.text)
    hashes=(line.split(':') for line in hashes.text.splitlines())
    for h,count in hashes:
        if h==hashe_to_check:
            return count
    return 0

def pwned_api_check(password):
    sha1password=hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    firts_five,tail=sha1password[:5],sha1password[5:]
    responds=request_api_data(firts_five)
    #print(responds.text)
    return get_password_leak_count(responds,tail)

def main(argv):
    for password in argv:
        count=pwned_api_check(password)
        if count:
            print(f'{password} was found {count} number of times.. you should change the password')
        else:
            print(f'{password} was not found.. you good to go')

if __name__=='__main__':
    main(sys.argv[1:])
    #main(pathlib.Path('pass.txt').read_text())


