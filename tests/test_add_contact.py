__author__ = 'eya'
from model.contact import Contact
import pytest
import random
import string

def random_string(maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_email(maxlen):
    symbols = string.ascii_letters + string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + "@ww.com"

testdata = [Contact(firstname="", lastname="", email="")] + [
    Contact(firstname=random_string(20), lastname=random_string(20), email=random_email(10))
    for i in range(2)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts)+1 == app.contact.count()
    old_contacts.append(contact)
    new_contacts = app.contact.get_contact_list()
    print(old_contacts)
    print(new_contacts)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
