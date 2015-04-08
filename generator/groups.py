__author__ = 'magic'
from model.group import Group
import random
import string, re
import os.path
import jsonpickle
import getopt, sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/groups.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    s = "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
    return re.sub("\s\s+", " ", s)

testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as output:
    jsonpickle.set_encoder_options("json", indent=2)
    output.write(jsonpickle.encode(testdata))