__author__ = 'eya'

from model.contact import Contact

def test_add_contact(app):
    app.contact.open_add_contact_page()
    app.contact.fill_in_new_contact_form(Contact("one", "two", "three", "four", "one.threetwo@ww.com"))
