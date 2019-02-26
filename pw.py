import string
import random


def password():
    pw = []
    #pw = pw + ([random.choice(string.punctuation)])
    pw = pw + ([random.choice(string.digits)])
    pw = pw + ([random.choice(string.ascii_uppercase)])
    pw = pw + ([random.choice(string.ascii_lowercase)])
    for i in range(5):
        # pw = pw + ([random.choice(string.punctuation + string.ascii_letters + string.digits)])
        pw = pw + ([random.choice(string.ascii_letters + string.digits)])
    random.shuffle(pw)
    pw = ''.join(pw)
    print(pw)


number1 = input("first number? ")
password()