import string
import random

def upper_char():
    letters = ""
    for i in range(2):
        k = random.choice(string.ascii_uppercase)
        letters+=k
    return letters

def lower_char():
    letters = ""
    for i in range(4):
        k = random.choice(string.ascii_lowercase)
        letters += k
    return letters

def symbol():
    symbol_table = ["!","@","#","$","&"]
    return random.choice(symbol_table)

def number():
    numbers = ""
    for i in range(3):
        k = random.randint(0,9)
        numbers+=str(k)
    return numbers

def shuffle(arrray):
    return random.shuffle(arrray)

def create(r):
    password = ""
    for i in range(len(r)):
        password+=r[i]
    return password

def generate_password():
    u = upper_char()
    l = lower_char()
    s = symbol()
    n = number()
    choices = [u,l,s,n]
    random.shuffle(choices)
    password = create(choices)
    return password



p = generate_password()
print(p)
