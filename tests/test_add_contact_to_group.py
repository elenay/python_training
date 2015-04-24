__author__ = 'eya'
from model.contact import Contact
from model.group import Group
from fixture.orm import OrmFixture
import random

db = OrmFixture(host="127.0.0.1", name="addressbook", user="root", password="")

def test_add_contact_to_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="GroupForContact"))
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="NoOneWasHere"))
    old_contacts = db.get_contact_list()
    if app.contact.check_presence_contact_not_in_group() is True:
        contacts_not_in_group = db.get_contacts_not_in_group()
        added_contact = random.choice(contacts_not_in_group)
    else:
        app.contact.create(Contact(firstname="EmptyGroup"))
    app.contact.add_contact_by_id_to_group(added_contact.id)
    assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_delete_contact_from_group(app, db):
    pass
