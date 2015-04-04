__author__ = 'eya'
from model.contact import Contact
import pytest
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
