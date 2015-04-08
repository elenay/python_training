__author__ = 'magic'
from model.contact import Contact
import random
import string, re

def random_string(maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    s = "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]).strip()
    return re.sub("\s\s+", " ", s)

testdata = [Contact(firstname=firstname, lastname=lastname, email=email)
    for firstname in ["", random_string(10)]
    for lastname in ["", random_string(20)]
    for email in ["", random_string(20)]]