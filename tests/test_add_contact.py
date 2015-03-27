__author__ = 'eya'

from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="created", lastname="two", email="one.threetwo@ww.com")
    contact.id = old_contacts[0].id
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts)+1 == len(new_contacts)
    #old_contacts.append(contact)
    old_contacts[0] = contact
    print (old_contacts)
    print (new_contacts)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
