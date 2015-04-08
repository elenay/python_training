__author__ = 'magic'
from model.contact import Contact
import random
import string, re
import os.path
import jsonpickle
import getopt, sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(maxlen):
    symbols = string.ascii_letters + string.digits
    s = "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
    return re.sub("\s\s+", " ", s)

testdata = [Contact(firstname="", lastname="", email="")] + [
    Contact(firstname=random_string(10), lastname=random_string(20), email=random_string(20))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as output:
    jsonpickle.set_encoder_options("json", indent=2)
    output.write(jsonpickle.encode(testdata))