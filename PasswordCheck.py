import requests
import hashlib
import sys

'''

This small project is meant to check if the inputted password has been pwned.

'''

def request_api_data(hashedpass):

    url = 'https://api.pwnedpasswords.com/range/{}'.format(hashedpass)
    req = requests.get(url)
    if req.status_code!=200:
        raise Exception('Error, kindly check the input and retry')
    return req

def leaked_pass_count(hashes, hash_to_check):
    hashes=(line.split(':') for line in hashes.text.splitlines())
    for hash,count in hashes:
        if hash==hash_to_check:
            return count
    return 0

def api_check(password):
    sha1password=hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail=sha1password[:5], sha1password[5:]
    response=request_api_data(first5_char)
    return leaked_pass_count(response,tail)


def main(args):
    # with open ('passwrd','r') as p:
    #     for word in [x.strip() for x in p.readlines()]:
    #         count=api_check(word)
    #         if count:
    #             print('{} was found {}  times, you should probably change it'.format(word,count))
    #         else:
    #             print('{} was not found, continue!'.format(word))
    for password in args:
        count=api_check(password)
        if count:
            print('{} was found {}  times, you should probably change it'.format(password,count))
        else:
            print('{} was not found, continue!'.format(password))

if __name__=="__main__":
    main(sys.argv[1:])