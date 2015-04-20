__author__ = 'eya'
import re
from model.contact import Contact


def test_all_fields_on_edit_page(app, db):
    contacts_from_db = db.get_contact_list()
    index = range(len(contacts_from_db))
    contacts_from_edit_page = []
    for i in index:
        contact_from_edit_page = app.contact.get_contact_info_from_edit_page(i)
        contacts_from_edit_page.append(contact_from_edit_page)
    assert sorted(contacts_from_db, key=Contact.id_or_max) == sorted(contacts_from_edit_page, key=Contact.id_or_max)


def test_all_fields_on_home_page(app, db):
    contacts_from_home_page = app.contact.get_contact_list()
    db_contacts = db.get_contact_list()
    assert sorted(contacts_from_home_page, key=Contact.id_or_max) == sorted(db_contacts, key=Contact.id_or_max)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x !="",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x !="",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))